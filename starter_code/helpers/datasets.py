"""
Frame readers for the LeRobot robotics datasets used across the starter exercises.

WHY THIS EXISTS
---------------
Both datasets we use are LeRobot repos whose camera frames are stored as out-of-band,
AV1-encoded MP4 videos under ``videos/…`` — NOT as an image column in the parquet:

    jesbu1/bridge_v2_lerobot       BridgeData V2, WidowX arm   (codebase v2.0, one MP4/episode)
    lerobot/svla_so100_pickplace   SO-100 pick-place demos     (codebase v3.0, chunked MP4 files)

So ``datasets.load_dataset(repo)[i]["image"]`` does NOT work — there is no image column,
which is exactly why the previous starter code raised ``StopIteration`` hunting for one.

Instead we read ``meta/info.json`` to find the camera key + the ``video_path`` template,
download ONE small MP4 with ``huggingface_hub``, and decode its frames.

DECODING
--------
OpenCV (``cv2.VideoCapture``) is the primary decoder and handles the image ops. BUT the
``opencv-python`` pip wheel's bundled ffmpeg has no *software* AV1 decoder, and these videos
are AV1 — so for AV1 we decode with ``imageio`` + ``imageio-ffmpeg`` (whose bundled ffmpeg
does handle AV1). Both are pip-only; no ``av``/PyAV and no system ffmpeg required. Which
decoder runs first is chosen per-video from the codec in ``meta/info.json``; the other is a
fallback. huggingface_hub caches every download, so repeat calls are instant/offline.
"""

from __future__ import annotations

import json
import os
import string
from functools import lru_cache

import numpy as np

BRIDGE = "jesbu1/bridge_v2_lerobot"
SVLA = "lerobot/svla_so100_pickplace"

# Keep the whole-file decode bounded so the one-time cache build never runs away on the
# big chunked videos (each SO-100 file packs up to ~1000 episodes).
_MAX_SCAN = 3000


def _hub_download(repo_id: str, filename: str) -> str:
    """Download one file from a HF *dataset* repo and return its local (cached) path."""
    from huggingface_hub import hf_hub_download

    return hf_hub_download(repo_id=repo_id, filename=filename, repo_type="dataset")


@lru_cache(maxsize=8)
def _info(repo_id: str) -> dict:
    with open(_hub_download(repo_id, "meta/info.json"), encoding="utf-8") as fh:
        return json.load(fh)


def camera_keys(repo_id: str) -> list:
    """The dataset's video feature keys, e.g. ['observation.images.top', ...]."""
    feats = _info(repo_id).get("features", {})
    return [
        k for k, v in feats.items() if isinstance(v, dict) and v.get("dtype") == "video"
    ]


def _codec(repo_id: str, camera: str) -> str:
    try:
        return _info(repo_id)["features"][camera]["info"]["video.codec"].lower()
    except Exception:
        return ""


def _template_fields(template: str) -> list:
    return [name for _, name, _, _ in string.Formatter().parse(template) if name]


def _video_rel_path(repo_id: str, camera: str, episode: int) -> str:
    """Repo-relative path of the MP4 holding ``episode`` for ``camera`` (any layout)."""
    info = _info(repo_id)
    template = info["video_path"]
    chunk_size = int(info.get("chunks_size", 1000)) or 1000
    chunk = episode // chunk_size
    values = {
        "video_key": camera,
        "episode_index": episode,
        "episode_chunk": chunk,
        "chunk_index": chunk,
        "file_index": 0,  # v3.0 packs many episodes per file; the first file is plenty
    }
    return template.format(**{f: values.get(f, 0) for f in _template_fields(template)})


# ── decoders ──────────────────────────────────────────────────────────────────
def _iter_cv2(path: str):
    """Yield RGB uint8 frames via OpenCV. Handles common codecs; on AV1 the pip wheel
    yields nothing (no software AV1 decoder) and we fall back to imageio."""
    import cv2

    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        cap.release()
        return
    try:
        while True:
            ok, bgr = cap.read()
            if not ok:
                break
            yield bgr[:, :, ::-1]  # BGR -> RGB
    finally:
        cap.release()


def _iter_imageio(path: str):
    """Yield RGB uint8 frames via imageio + imageio-ffmpeg (decodes AV1)."""
    import imageio

    reader = imageio.get_reader(path)  # ffmpeg backend
    try:
        for frame in reader:
            yield np.asarray(frame)
    finally:
        reader.close()


def _frames(
    path: str, want: int, stride: int = 1, max_scan=None, prefer_cv2: bool = True
) -> list:
    """Return up to ``want`` RGB PIL frames, keeping every ``stride``-th. Tries the preferred
    decoder first (OpenCV for most codecs, imageio for AV1) and the other as a fallback."""
    from PIL import Image

    sources = (_iter_cv2, _iter_imageio) if prefer_cv2 else (_iter_imageio, _iter_cv2)
    for source in sources:
        out: list = []
        try:
            for i, arr in enumerate(source(path)):
                if max_scan is not None and i >= max_scan:
                    break
                if stride <= 1 or i % stride == 0:
                    out.append(
                        Image.fromarray(np.ascontiguousarray(arr, dtype=np.uint8))
                    )
                    if len(out) >= want:
                        break
        except Exception:
            out = []
        if out:
            return out
    return []


def _frame_count(path: str) -> int:
    """Total frames from the container metadata (works even when cv2 can't decode the pixels)."""
    try:
        import cv2

        cap = cv2.VideoCapture(path)
        try:
            return int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
        finally:
            cap.release()
    except Exception:
        return 0


def scene_frames(
    repo_id: str = BRIDGE, n: int = 200, camera: str | None = None
) -> list:
    """
    Return up to ``n`` RGB PIL frames of real robot scenes from ``repo_id``.

    * Per-episode layouts (BridgeData V2) walk consecutive episode MP4s until ``n`` frames
      are collected.
    * Chunked layouts (SO-100) sample frames spread across the first file, so the frames
      stand in for distinct trajectories rather than one instant.
    """
    info = _info(repo_id)
    cams = camera_keys(repo_id)
    cam = camera or (cams[0] if cams else None)
    if cam is None:
        raise RuntimeError(f"{repo_id}: meta/info.json exposes no 'video' feature")

    prefer_cv2 = (
        _codec(repo_id, cam) != "av1"
    )  # AV1 -> imageio first (opencv can't decode it)
    fields = _template_fields(info["video_path"])
    frames: list = []

    if "episode_index" in fields:  # one MP4 per episode (v2.0)
        total = int(info.get("total_episodes", 10**9))
        episode = 0
        while len(frames) < n and episode < total:
            try:
                path = _hub_download(repo_id, _video_rel_path(repo_id, cam, episode))
            except Exception:
                break
            frames.extend(_frames(path, n - len(frames), prefer_cv2=prefer_cv2))
            episode += 1
    else:  # many episodes per file (v3.0)
        path = _hub_download(repo_id, _video_rel_path(repo_id, cam, 0))
        total = _frame_count(path)
        span = min(total, _MAX_SCAN) if total else _MAX_SCAN
        stride = max(1, span // max(1, n))
        frames = _frames(
            path, n, stride=stride, max_scan=_MAX_SCAN, prefer_cv2=prefer_cv2
        )

    if not frames:
        raise RuntimeError(
            f"{repo_id}: decoded 0 frames. Check your network and that imageio-ffmpeg is "
            f"installed (`pip install imageio imageio-ffmpeg`) — these videos are AV1, which "
            f"opencv-python's bundled ffmpeg cannot software-decode."
        )
    return frames[:n]
