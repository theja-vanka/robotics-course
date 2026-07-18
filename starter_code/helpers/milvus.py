"""A clean, file-based Milvus (pymilvus-lite) — no Docker, no server to start."""

from __future__ import annotations

import os
import shutil

from pymilvus import MilvusClient

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # starter_code/
_DB = os.path.join(_ROOT, "milvus_demo.db")


def fresh_client() -> MilvusClient:
    """
    Return a brand-new local Milvus client, wiping any previous demo DB first so each test
    starts clean.

    NOTE: MilvusClient stores its data as a DIRECTORY, so it must be removed with
    ``shutil.rmtree()`` — ``os.remove()`` raises IsADirectoryError on the second run.
    """
    if os.path.exists(_DB):
        shutil.rmtree(_DB)
    return MilvusClient(_DB)
