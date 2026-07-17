"""
CLIP / DINOv2 embeddings of the robot-scene frames, cached to .npy in ``starter_code/``.

The first call downloads a model + a few small MP4s and writes the cache; every later call
(across all days) loads the .npy instantly. Delete the .npy to force a rebuild.
"""

from __future__ import annotations

import os

import numpy as np

from .datasets import BRIDGE, SVLA, scene_frames
from .runtime import DEVICE

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # starter_code/


def _cache(name: str) -> str:
    return os.path.join(_ROOT, name)


def _clip_encode(images, batch: int = 32) -> np.ndarray:
    import torch
    from transformers import CLIPModel, CLIPProcessor

    proc = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(DEVICE).eval()
    vecs = []
    with torch.no_grad():
        for i in range(0, len(images), batch):
            b = proc(images=images[i : i + batch], return_tensors="pt", padding=True)
            b = {k: v.to(DEVICE) for k, v in b.items()}
            vecs.append(model.get_image_features(**b).cpu().numpy())
    return np.vstack(vecs).astype("float32")


def _dinov2_encode(images, batch: int = 16) -> np.ndarray:
    import torch
    from transformers import AutoImageProcessor, AutoModel

    proc = AutoImageProcessor.from_pretrained("facebook/dinov2-base")
    model = AutoModel.from_pretrained("facebook/dinov2-base").to(DEVICE).eval()
    vecs = []
    with torch.no_grad():
        for i in range(0, len(images), batch):
            b = proc(images=images[i : i + batch], return_tensors="pt")
            b = {k: v.to(DEVICE) for k, v in b.items()}
            vecs.append(model(**b).last_hidden_state[:, 0].cpu().numpy())  # CLS token
    return np.vstack(vecs).astype("float32")


def clip_bridge_embeddings(n: int = 200):
    """(vectors, query, dim, count) — CLIP ViT-B/32 over BridgeData V2 scenes, cached."""
    path = _cache("clip_bridge_embeddings.npy")
    if not os.path.exists(path):
        print("[helpers] building CLIP BridgeData V2 embeddings (one-time)…")
        np.save(path, _clip_encode(scene_frames(BRIDGE, n)))
    vecs = np.load(path)
    return vecs, vecs[0], int(vecs.shape[1]), len(vecs)


def dinov2_bridge_embeddings(n: int = 200):
    """(vectors, query, dim, count) — DINOv2-base CLS features over BridgeData V2, cached."""
    path = _cache("dinov2_bridge_embeddings.npy")
    if not os.path.exists(path):
        print("[helpers] building DINOv2 BridgeData V2 embeddings (one-time)…")
        np.save(path, _dinov2_encode(scene_frames(BRIDGE, n)))
    vecs = np.load(path)
    return vecs, vecs[0], int(vecs.shape[1]), len(vecs)


def demo_episode_embeddings(max_eps: int = 64):
    """
    (vectors, episode_ids, query, dim, count) — CLIP over SO-100 pick-place demo key-frames,
    cached. ``episode_ids`` are the per-key-frame indices used by the Days 13–16 exercises.
    """
    path, ep_path = _cache("demo_traj_embeddings.npy"), _cache("demo_episode_ids.npy")
    if not os.path.exists(path):
        print("[helpers] building CLIP SO-100 demo embeddings (one-time)…")
        frames = scene_frames(SVLA, max_eps)
        np.save(path, _clip_encode(frames))
        np.save(ep_path, np.arange(len(frames)))
    vecs = np.load(path)
    episode_ids = np.load(ep_path).tolist()
    return vecs, episode_ids, vecs[0], int(vecs.shape[1]), len(vecs)
