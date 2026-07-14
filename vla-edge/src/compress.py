"""Compress the fine-tuned policy + measure the deltas.  Capstone W7 ⭐   Run: python src/compress.py

Runs today: prints a correct 4-bit config (if libs present) and shows the measure()
helper you'll call BEFORE and AFTER compressing. The number that matters is the delta.
"""
from __future__ import annotations
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CFG


def bnb_4bit_config():
    """4-bit NF4 load config (QLoRA-style) — the easy, correct first compression step."""
    import torch
    from transformers import BitsAndBytesConfig
    return BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )


def measure(module, example_input, runs: int = 50) -> dict:
    """Generic size + latency probe. Run it on the fp16 model, then the 4-bit model."""
    n_params = sum(p.numel() for p in module.parameters())
    size_mb = sum(p.numel() * p.element_size() for p in module.parameters()) / 1e6
    for _ in range(5):
        module(example_input)
    t0 = time.perf_counter()
    for _ in range(runs):
        module(example_input)
    ms = (time.perf_counter() - t0) / runs * 1000
    return {"params_M": round(n_params / 1e6, 2), "size_MB": round(size_mb, 1), "latency_ms": round(ms, 2)}


def _get_example_obs():
    """PROVIDED: load one real observation from lerobot/svla_so100_pickplace.

    Returns a dict you can pass to `policy.predict(obs)` (and hence to measure()).
    Uses the same dataset the LoRA fine-tune trains on, so the input distribution matches.

    Example:
        obs = _get_example_obs()
        from policy import VLAPolicy
        pol = VLAPolicy(); pol.load()
        measure(pol.model, obs)   # 'before' numbers

    The returned dict:
        {
          "observation.images.laptop": PIL.Image (640×480 tabletop scene),
          "observation.state":         list[float] (6 joint angles),
          "instruction":               "pick up the cube and place it in the box",
        }
    """
    from datasets import load_dataset
    ds  = load_dataset("lerobot/svla_so100_pickplace", split="train")
    cam = next(k for k in ds.column_names if k.startswith("observation.images."))
    row = ds[0]
    return {
        cam:                  row[cam].convert("RGB"),
        "observation.state":  row["observation.state"],
        "instruction":        CFG.task,
    }


def compress_model():
    """TODO ⭐: compress your fine-tuned policy and record the delta.

    Use _get_example_obs() (PROVIDED above) as your example_input for measure():

        obs = _get_example_obs()

        # ── BEFORE ────────────────────────────────────────────────────────
        from policy import VLAPolicy
        pol_fp16 = VLAPolicy(); pol_fp16.load()
        before = measure(pol_fp16.model, obs)
        from eval import log_row; log_row("fp16", before)

        # ── AFTER (4-bit NF4) ─────────────────────────────────────────────
        from transformers import AutoModelForVision2Seq
        pol_4bit = AutoModelForVision2Seq.from_pretrained(
            CFG.base_model,
            quantization_config=bnb_4bit_config(),   # PROVIDED
            device_map="auto",
        )
        after = measure(pol_4bit, obs)
        log_row("4bit_nf4", after)

        print(f"size  {before['size_MB']:.0f} MB  →  {after['size_MB']:.0f} MB")
        print(f"speed {before['latency_ms']:.1f} ms →  {after['latency_ms']:.1f} ms")

    bnb_4bit_config() and measure() above are PROVIDED — call them.
    """
    # 👇 write your code here, then DELETE the line below
    raise NotImplementedError("TODO ⭐: compress the model and record before/after")


def main():
    print("Compression ladder:  fp16 → 4-bit NF4 (bitsandbytes) → GPTQ/AWQ → TensorRT-NVFP4")
    try:
        print("4-bit config (provided):", bnb_4bit_config())
    except ImportError:
        print("  (pip install bitsandbytes transformers torch — bnb needs an NVIDIA GPU)")
    compress_model()  # ← stops here until you implement it


if __name__ == "__main__":
    main()
