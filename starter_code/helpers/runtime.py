"""The one compute device every model preamble uses: CUDA -> MPS (Apple) -> CPU."""

from __future__ import annotations

import torch

DEVICE = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)
