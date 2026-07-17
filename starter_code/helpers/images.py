"""One real robot-scene image (PIL) for the vision / hands-on exercises."""

from __future__ import annotations

from .datasets import BRIDGE, scene_frames


def load_scene_image(size=None):
    """
    Return a BridgeData V2 / WidowX RGB frame as a PIL image.

    Pass ``size=(w, h)`` (e.g. ``(512, 512)``) to resize for Stable Diffusion / ControlNet.
    """
    img = scene_frames(BRIDGE, 1)[0]
    return img.resize(size) if size else img
