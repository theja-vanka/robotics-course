# 🧩 Starter Code — fill the functions, then `pytest` yourself

57 skeletons, one per coding block, laid out as `DayNN/<name>.py` (one folder per day, no `DayNN_` prefix). Each file imports its **shared setup** from the `helpers/` package — a real robotics dataset is loaded and embedded for you — then splits the task into **functions you fill**, and ships **pytest tests** so `pytest <file>` tells you pass/fail.

## Layout

```
starter_code/
  helpers/       ← shared, PROVIDED code (dataset readers, CLIP/DINOv2, Milvus, bench)
  conftest.py    ← lets `from helpers import …` work from any DayNN/ folder
  Day01/ … Day29/  ← the fill-in-the-function exercises
  *.npy          ← embedding caches, built once on first run, shared across days
```

## How to use
1. Open today's file (the Day note's **▶️ DO THIS** says which), e.g. `Day03/index_types.py`.
2. Fill the first function; delete its `raise` line.
3. Check yourself: `pytest Day03/index_types.py` (or `python Day03/index_types.py`).
4. Green = passed. Keep going until all tests pass, then tick the Day-note boxes.

First run downloads a model + a few small robot-scene videos and writes an embedding cache (`*.npy`) up one level in `starter_code/`; every later run loads it instantly.

> The day stubs are generated — re-create them any time with `python build_starters.py` (it rewrites the `DayNN/` folders + this README). The `helpers/` package is hand-maintained shared library code and is **not** overwritten. Install deps with `pip install -r requirements.txt`. Tests needing an external repo/GPU are marked skipped.

## Index

| Day | Session | Task | File | Install |
|---|---|---|---|---|
| Day01 | 🛠️ Hands-on | Python Tooling | `Day01/python_tooling.py` | `torch` |
| Day01 | 🔧 Build + Milvus | First Collection | `Day01/first_collection.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day02 | 🛠️ Hands-on | Run LLaVA on Robot Scenes | `Day02/run_llava_on_robot_scenes.py` | `transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day02 | 🔧 Build + Milvus | Store CLIP Embeddings | `Day02/store_clip_embeddings.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day02 | 🗜️ Compression | FP16 | `Day02/fp16.py` | `torch torchvision pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day03 | 🛠️ Hands-on | Run Stable Diffusion img2img | `Day03/run_stable_diffusion_img2img.py` | `diffusers transformers accelerate pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day03 | 🔧 Build + Milvus | Index Types | `Day03/index_types.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day03 | 🗜️ Compression | INT8 PTQ | `Day03/int8_ptq.py` | `torch torchvision pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day04 | 🛠️ Hands-on | Run SAM 2 on Robot Scene | `Day04/run_sam_2_on_robot_scene.py` | `ultralytics pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day04 | 🔧 Build + Milvus | DINOv2 Object Store | `Day04/dinov2_object_store.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day05 | 🛠️ Hands-on | Train 3DGS with Nerfstudio | `Day05/train_3dgs_with_nerfstudio.py` | `nerfstudio` |
| Day05 | 🔧 Build + Milvus | Production Schema Design | `Day05/production_schema_design.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day05 | 🗜️ Compression | Pruning Hands-on | `Day05/pruning_hands_on.py` | `torch torchvision pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day06 | 🔧 Build + Milvus | Scene Retrieval Service | `Day06/scene_retrieval_service.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day07 | 🛠️ Hands-on | Fine-tune YOLOv8 on YCB Dataset | `Day07/fine_tune_yolov8_on_ycb_dataset.py` | `ultralytics pytest` |
| Day07 | 🔧 Build + Milvus | Detection Embedding Store | `Day07/detection_embedding_store.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day07 | 🗜️ Compression | Distillation Hands-on | `Day07/distillation_hands_on.py` | `torch torchvision pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day08 | 🛠️ Hands-on | Run Depth Anything v2 + Point Cloud | `Day08/run_depth_anything_v2_point_cloud.py` | `transformers pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day08 | 🔧 Build + Milvus | Multi-modal (RGB + Depth) | `Day08/multi_modal_rgb_depth.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day08 | 🗜️ Compression | ONNX Export | `Day08/onnx_export.py` | `onnxruntime torch torchvision numpy pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day09 | 🛠️ Hands-on | Run MegaPose on YCB Object | `Day09/run_megapose_on_ycb_object.py` | `# clone the pose repo (see resources)` |
| Day09 | 🔧 Build + Milvus | Object Pose Library | `Day09/object_pose_library.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day09 | 🗜️ Compression | TensorRT Basics | `Day09/tensorrt_basics.py` | `onnxruntime torch torchvision numpy pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day10 | 🛠️ Hands-on | Run AnyGrasp on Point Cloud | `Day10/run_anygrasp_on_point_cloud.py` | `# clone the grasp repo (see resources)` |
| Day10 | 🔧 Build + Milvus | Grasp Pose Library | `Day10/grasp_pose_library.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day10 | 🗜️ Compression | TensorRT FP16 | `Day10/tensorrt_fp16.py` | `onnxruntime torch torchvision numpy pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day11 | 🛠️ Hands-on | Run ORB-SLAM3 on TUM RGB-D | `Day11/run_orb_slam3_on_tum_rgb_d.py` | `# mostly C++ (ORB-SLAM3)` |
| Day11 | 🔧 Build + Milvus | Semantic SLAM Map | `Day11/semantic_slam_map.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day11 | 🗜️ Compression | TensorRT INT8 | `Day11/tensorrt_int8.py` | `onnxruntime torch torchvision numpy pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day12 | 🔧 Build + Milvus | Pipeline + Milvus Integration | `Day12/pipeline_milvus_integration.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day12 | 🗜️ Compression | Benchmark Table | `Day12/benchmark_table.py` | `torch torchvision pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day13 | 🛠️ Hands-on | Load & Run a VLA (SmolVLA-first) | `Day13/load_run_a_vla_smolvla_first.py` | `lerobot transformers numpy` |
| Day13 | 🔧 Build + Milvus | Retrieval-Augmented VLA | `Day13/retrieval_augmented_vla.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day13 | 🗜️ Compression | Attention Head Pruning | `Day13/attention_head_pruning.py` | `torch` |
| Day14 | 🛠️ Hands-on | Fine-tune a VLA (SmolVLA) with LoRA | `Day14/fine_tune_a_vla_smolvla_with_lora.py` | `lerobot transformers peft` |
| Day14 | 🔧 Build + Milvus | Demo Replay Buffer | `Day14/demo_replay_buffer.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day14 | 🗜️ Compression | LoRA + QLoRA | `Day14/lora_qlora.py` | `torch` |
| Day15 | 🛠️ Hands-on | Load & Amplify Demo Episodes | `Day15/load_amplify_demo_episodes.py` | `lerobot numpy` |
| Day15 | 🔧 Build + Milvus | Demo-Episode Deduplication | `Day15/demo_episode_deduplication.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day15 | 🗜️ Compression | Low-rank Factorisation | `Day15/low_rank_factorisation.py` | `torch` |
| Day16 | 🔧 Build + Milvus | Demo-Episode Browser | `Day16/demo_episode_browser.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day17 | 🛠️ Hands-on | Depth-conditioned ControlNet Augmentation | `Day17/depth_conditioned_controlnet_augmentation.py` | `diffusers transformers accelerate pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day17 | 🔧 Build + Milvus | Diversity-guided Augmentation | `Day17/diversity_guided_augmentation.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day18 | 🛠️ Hands-on | Run DreamerV3 | `Day18/run_dreamerv3.py` | `# clone DreamerV3 (see resources)` |
| Day18 | 🔧 Build + Milvus | World Model State Memory | `Day18/world_model_state_memory.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day18 | 🗜️ Compression | Flash Attention & Speculative Decoding | `Day18/flash_attention_speculative_decoding.py` | `torch` |
| Day19 | 🛠️ Hands-on | 3DGS Scene + Grasp Poses | `Day19/3dgs_scene_grasp_poses.py` | `nerfstudio` |
| Day19 | 🔧 Build + Milvus | 3DGS Object Index | `Day19/3dgs_object_index.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day19 | 🗜️ Compression | 4-bit Quantisation (GPTQ/AWQ) | `Day19/4_bit_quantisation_gptq_awq.py` | `torch` |
| Day20 | 🗜️ Compression | Compress the Pipeline | `Day20/compress_the_pipeline.py` | `torch torchvision pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day21 | 🛠️ Hands-on | Implement Attention from Scratch | `Day21/implement_attention_from_scratch.py` | `torch numpy` |
| Day21 | 🔧 Build + Milvus | ANN Benchmarking | `Day21/ann_benchmarking.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day21 | 🗜️ Compression | Speculative Decoding Hands-on | `Day21/speculative_decoding_hands_on.py` | `` |
| Day22 | 🛠️ Hands-on | Add Latency Profiler | `Day22/add_latency_profiler.py` | `` |
| Day23 | 🛠️ Hands-on | Custom PyTorch Dataset | `Day23/custom_pytorch_dataset.py` | `torch` |
| Day23 | 🔧 Build + Milvus | Anomaly Detection | `Day23/anomaly_detection.py` | `"pymilvus[milvus_lite]" numpy transformers torch pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
| Day29 | 🗜️ Compression | Final Benchmark | `Day29/final_benchmark.py` | `torch torchvision pillow opencv-python-headless imageio imageio-ffmpeg huggingface_hub` |
