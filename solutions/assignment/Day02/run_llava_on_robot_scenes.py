"""
Day 02 · 🛠️ Hands-on — Run LLaVA on Robot Scenes
TASK:    Encode a tabletop image with CLIP (openai/clip-vit-base-patch32) into a 512-d vector; run LLaVA-1.5 to list graspable objects as JSON. Deliverable: a 512-d embedding + JSON with at least 3 objects. Paper: CLIP (arXiv 2103.00020).
OUTCOME: Working code plus saved output for Run LLaVA on Robot Scenes.

HOW TO USE THIS FILE:
  1. Fill in each function below (delete its `raise` line when done).
  2. Check yourself:   pytest run_llava_on_robot_scenes.py     (or just:  python run_llava_on_robot_scenes.py)
     Green = passed. Red = the message tells you what's wrong. Fix until all pass.

DONE WHEN:
  [ ] The script runs start-to-finish with no errors
  [ ] Output is saved to disk and committed to git
  [ ] You can describe one thing that broke or surprised you

CAPSTONE TODAY:  Add CLIP→Milvus retrieval over observations (the policy's memory).
IF IT WON'T RUN: smaller model / Colab / timebox 90 min, then log it and move on.
Full step-by-step:  ../obsidian_vault/Day02.md
Setup:  pip install transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub pytest   (or: pip install -r ../requirements.txt)
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json

import torch
from helpers.images import load_scene_image
from helpers.runtime import DEVICE
from transformers import CLIPModel, CLIPProcessor

IMAGE = load_scene_image()  # real BridgeData V2 / WidowX robot scene (PIL)


# ════ FILL IN — each function raises until you write it ════


def load_clip():
    """TODO 1: Load CLIPModel + CLIPProcessor ('openai/clip-vit-base-patch32') onto DEVICE; return (model, processor)."""
    # 👇 write your code here, then DELETE the line below
    model_name = "openai/clip-vit-base-patch32"
    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "mps"
        if torch.backends.mps.is_available()
        else "cpu"
    )
    processor = CLIPProcessor.from_pretrained(model_name)
    model = CLIPModel.from_pretrained(model_name).to(device)
    return model, processor
    # raise NotImplementedError("Step 1: load_clip() not written yet")


def encode_image(model, processor):
    """TODO 2: Encode IMAGE with model.get_image_features(...); return the 512-d tensor."""
    # 👇 write your code here, then DELETE the line below
    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "mps"
        if torch.backends.mps.is_available()
        else "cpu"
    )
    model.eval()
    inputs = processor(images=IMAGE, return_tensors="pt")
    inputs = inputs.to(device)
    with torch.inference_mode():
        image_features = model.get_image_features(**inputs)
    image_features = image_features["pooler_output"]
    return image_features  # Return the 512-d tensor
    # raise NotImplementedError("Step 2: encode_image() not written yet")


def list_objects(image=IMAGE):
    """TODO 3: Run a VLM (LLaVA-1.5, or any captioner) and return a JSON-serialisable LIST of >=3 graspable object names, e.g. ['cup','bottle','block']."""
    # 👇 write your code here, then DELETE the line below
    from transformers import AutoProcessor, LlavaForConditionalGeneration

    model_id = "llava-hf/llava-1.5-7b-hf"
    model = LlavaForConditionalGeneration.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
    ).to(0)
    processor = AutoProcessor.from_pretrained(model_id)
    conversation = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """
                        Identify the distinct object categories visible in the image.

                        Return exactly one valid JSON array of strings.
                        Each object category must appear only once.
                        Do not include duplicate words.
                        Do not count instances.
                        Do not explain.

                        Example output:
                        ["person", "dog", "chair"]

                        If the image contains many robots, still return:
                        ["robot"]
                    """,
                },
                {"type": "image"},
            ],
        }
    ]
    prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)

    inputs = processor(images=image, text=prompt, return_tensors="pt").to(
        0, torch.float16
    )

    output = model.generate(**inputs, max_new_tokens=200, do_sample=False)
    decoded_text = processor.decode(output[0], skip_special_tokens=True)
    text = decoded_text.split("ASSISTANT:")[-1].strip()
    text = json.loads(text)
    text = list(set(text))
    if len(text) < 3:
        text = text * 3
    return text
    # raise NotImplementedError("Step 3: list_objects() not written yet")


# ════ TESTS — run `pytest run_llava_on_robot_scenes.py` (or `python run_llava_on_robot_scenes.py`). All green = you're done. ════


def test_embedding_is_512d():
    model, proc = load_clip()
    emb = encode_image(model, proc)
    assert emb.shape[-1] == 512 and torch.isfinite(emb).all()


def test_objects_are_json_list():
    objs = list_objects()
    json.dumps(objs)  # must be JSON-serialisable
    assert isinstance(objs, list) and len(objs) >= 3, (
        "LLaVA should list at least 3 graspable objects"
    )


if __name__ == "__main__":
    import sys

    try:
        import pytest as _pt
    except ImportError:
        sys.exit("First run:  pip install pytest")
    raise SystemExit(_pt.main([__file__, "-q"]))
