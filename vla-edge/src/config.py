"""Central config for the vla-edge capstone. Tune these, not the modules."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


@dataclass
class Config:
    # ── Model — start SMALL. SmolVLA-450M runs on a consumer/Colab GPU. ──
    base_model: str = "lerobot/smolvla_base"      # TODO: confirm the exact HF id you use
    device: str = "cuda"                           # "cpu" / "mps" if you have no NVIDIA GPU
    dtype: str = "float16"

    # ── Task / data ──
    dataset_repo_id: str = "lerobot/svla_so100_pickplace"  # a public LeRobot set; swap for yours
    task: str = "pick up the cube and place it in the box"

    # ── Fine-tune (LoRA) ──
    lora_r: int = 16
    lora_alpha: int = 32
    lora_dropout: float = 0.05
    lr: float = 1e-4
    steps: int = 2000
    batch_size: int = 8

    # ── Compression ──
    load_in_4bit: bool = True

    # ── Deploy / latency budget ──
    latency_budget_ms: float = 50.0
    warmup: int = 10
    timed_runs: int = 100

    # ── Paths ──
    adapter_dir: Path = field(default_factory=lambda: ROOT / "checkpoints" / "lora")
    bench_csv: Path = field(default_factory=lambda: ROOT / "benchmarks" / "results.csv")


CFG = Config()
