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
download ONE small MP4 with ``huggingface_hub``, and decode its frames with PyAV (which
ships its own ffmpeg incl. an AV1 decoder — no system ffmpeg and no heavy ``lerobot``
dependency). huggingface_hub caches every download, so repeat calls are instant/offline.
"""

from __future__ import annotations

import json
import os
import string
from functools import lru_cache

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


def _decode(path: str, want: int, stride: int = 1, max_scan: int | None = None) -> list:
    """Return up to ``want`` RGB PIL frames from an MP4, keeping every ``stride``-th frame."""
    import av

    frames: list = []
    with av.open(path) as container:
        try:
            container.streams.video[0].thread_type = "AUTO"
        except Exception:
            pass
        for i, frame in enumerate(container.decode(video=0)):
            if max_scan is not None and i >= max_scan:
                break
            if stride > 1 and (i % stride):
                continue
            frames.append(frame.to_image().convert("RGB"))
            if len(frames) >= want:
                break
    return frames


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
            frames.extend(_decode(path, n - len(frames)))
            episode += 1
    else:  # many episodes per file (v3.0)
        path = _hub_download(repo_id, _video_rel_path(repo_id, cam, 0))
        try:
            import av

            with av.open(path) as container:
                total = container.streams.video[0].frames or 0
        except Exception:
            total = 0
        span = min(total, _MAX_SCAN) if total else _MAX_SCAN
        stride = max(1, span // max(1, n))
        frames = _decode(path, n, stride=stride, max_scan=_MAX_SCAN)

    if not frames:
        raise RuntimeError(
            f"{repo_id}: decoded 0 frames — check your network connection and that PyAV "
            f"can decode AV1 (it ships its own ffmpeg; `pip install av`)."
        )
    return frames[:n]
