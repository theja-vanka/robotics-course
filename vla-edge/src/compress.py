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


def compress_model():
    """TODO ⭐: compress your fine-tuned policy and record the delta:
       1. load model fp16 -> measure(model, example_input)            # the 'before' numbers
       2. reload 4-bit:  AutoModel.from_pretrained(..., quantization_config=bnb_4bit_config())
       3. measure() again -> compare; log it with eval.log_row().
    bnb_4bit_config() and measure() above are PROVIDED — call them."""
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
