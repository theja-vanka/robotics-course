"""
Day 02 · 🔧 Build + Milvus — Store CLIP Embeddings
TASK:    Encode 100 robot images with CLIP. Insert 512-d vectors. Run similarity search. Log top-5.
OUTCOME: A working Milvus operation for Milvus — Store CLIP Embeddings.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest Day02_store_clip_embeddings.py     (or just:  python Day02_store_clip_embeddings.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The insert / query / operation completes without error
  [ ] Top-k results are sensible for your query
  [ ] Entity count + latency are written into your notes

CAPSTONE TODAY:  Add CLIP→Milvus retrieval over observations (the policy's memory).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day02.md
Setup:  pip install pymilvus numpy scikit-learn pytest
"""
from __future__ import annotations

import os
from datasets.features import image
from sklearn.datasets import load_digits   # OPEN dataset: 1797 handwritten digits (64-d), bundled with scikit-learn
from pymilvus import MilvusClient
from transformers import CLIPModel, CLIPProcessor

_DIGITS = load_digits()
EXAMPLE_VECTORS = _DIGITS.data.astype("float32")   # (1797, 64) REAL vectors stand in for your embeddings
QUERY = EXAMPLE_VECTORS[0]
DIM = EXAMPLE_VECTORS.shape[1]   # 64
N = len(EXAMPLE_VECTORS)         # 1797

def fresh_client():
    """PROVIDED: a clean local Milvus (file-based, no Docker)."""
    if os.path.exists("milvus_demo.db"):
        os.remove("milvus_demo.db")
    return MilvusClient(uri="http://localhost:19530")

DEVICE = "cuda"  # change to "cpu" or "mps" if you have no NVIDIA GPU


# ════ FILL IN — each function raises until you write it ════

def model_and_processor():
    model_name = "openai/clip-vit-base-patch32"
    model = CLIPModel.from_pretrained(model_name)
    processor = CLIPProcessor.from_pretrained(model_name)
    model.to(DEVICE)
    model.eval()
    return model, processor

def build_image_index(client):
    """TODO 1: Create collection 'clip_images' (vector dim DIM) and insert the FIRST 100 EXAMPLE_VECTORS — these stand in for 100 CLIP image embeddings. Return how many you inserted."""
    # 👇 write your code here, then DELETE the line below
    from PIL import Image
    import torch
    import time

    images = []

    for img in EXAMPLE_VECTORS[0:100]:
        # img shape: (8, 8), values: 0-16
        # scale to 0-255
        img = (img / img.max() * 255)
        # grayscale -> PIL -> RGB
        pil_img = Image.fromarray(img)
        pil_img = pil_img.convert("RGB")
        images.append(pil_img)

    model, processor = model_and_processor()

    encode_input = processor(images=images, return_tensors="pt").to(DEVICE)
    with torch.inference_mode():
        image_features = model.get_image_features(**encode_input)

    client.drop_collection(collection_name="clip_images")
    client.create_collection(
        collection_name="clip_images",
        dimension=image_features[0].shape[-1],
    )

    data = []
    for i, vector in enumerate(image_features.cpu().numpy().tolist()):
        data.append({"id": i, "vector": vector, "dataset": "digits"})
    res = client.insert(collection_name="clip_images", data=data)
    time.sleep(2)
    return len(res["ids"])
    raise NotImplementedError("Step 1: build_image_index() not written yet")


def search_similar(client, query=QUERY, k=5):
    """TODO 2: Return the ids of the k most similar images to `query` (your top-5 log)."""
    # 👇 write your code here, then DELETE the line below
    from PIL import Image
    import torch

    img = (query / query.max() * 255)
    pil_img = Image.fromarray(img)
    pil_img = pil_img.convert("RGB")

    model, processor = model_and_processor()
    encode_input = processor(images=[pil_img], return_tensors="pt").to(DEVICE)

    with torch.inference_mode():
        image_features = model.get_image_features(**encode_input)

    image_features = image_features.cpu().numpy().tolist()
    search_results = client.search(
        collection_name="clip_images",
        data=image_features,
        limit=5,
        Output_fields=["id", "dataset"],
    )
    return [result.id for result in search_results[0]]
    # raise NotImplementedError("Step 2: search_similar() not written yet")


# ════ TESTS — run `pytest Day02_store_clip_embeddings.py` (or `python Day02_store_clip_embeddings.py`). All green = you're done. ════

def test_indexed_100():
    c = fresh_client()
    assert build_image_index(c) == 100, "should index exactly the 100 image embeddings"

def test_topk_self():
    c = fresh_client(); build_image_index(c)
    ids = list(search_similar(c, EXAMPLE_VECTORS[0], 5))
    assert len(ids) == 5 and ids[0] == 0, "image 0 must be its own nearest neighbour"


if __name__ == "__main__":
    import sys
    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
