# 🧩 Starter Code — fill the functions, then `pytest` yourself

57 skeletons, one per coding block. Each **loads a specific model + an open-source dataset** (e.g. scikit-learn digits, the HF `cats-image`, a LeRobot set), splits the task into **functions** you fill, and ships **pytest tests** so running `pytest <file>` tells you pass/fail.

## How to use
1. Open today's file (the Day note's **▶️ DO THIS** says which).
2. Fill the first function; delete its `raise` line.
3. Check yourself: `pytest Day03_run_stable_diffusion_img2img.py` (or `python <file>`).
4. Green = passed. Keep going until all tests pass, then tick the Day-note boxes.

> Re-generate any time with `python build_starters.py`. Tests needing an external repo/GPU are marked skipped.

## Index

| Day | Session | Task | File | Install |
|---|---|---|---|---|
| Day01 | 🛠️ Hands-on | Python Tooling | `Day01_python_tooling.py` | `torch` |
| Day01 | 🔧 Build + Milvus | First Collection | `Day01_first_collection.py` | `pymilvus numpy scikit-learn` |
| Day02 | 🛠️ Hands-on | Run LLaVA on Robot Scenes | `Day02_run_llava_on_robot_scenes.py` | `transformers datasets torch pillow` |
| Day02 | 🔧 Build + Milvus | Store CLIP Embeddings | `Day02_store_clip_embeddings.py` | `pymilvus numpy scikit-learn` |
| Day02 | 🗜️ Compression | FP16 | `Day02_fp16.py` | `torch torchvision datasets pillow` |
| Day03 | 🛠️ Hands-on | Run Stable Diffusion img2img | `Day03_run_stable_diffusion_img2img.py` | `diffusers transformers accelerate datasets pillow` |
| Day03 | 🔧 Build + Milvus | Index Types | `Day03_index_types.py` | `pymilvus numpy scikit-learn` |
| Day03 | 🗜️ Compression | INT8 PTQ | `Day03_int8_ptq.py` | `torch torchvision datasets pillow` |
| Day04 | 🛠️ Hands-on | Run SAM 2 on Robot Scene | `Day04_run_sam_2_on_robot_scene.py` | `ultralytics datasets pillow` |
| Day04 | 🔧 Build + Milvus | DINOv2 Object Store | `Day04_dinov2_object_store.py` | `pymilvus numpy scikit-learn` |
| Day05 | 🛠️ Hands-on | Train 3DGS with Nerfstudio | `Day05_train_3dgs_with_nerfstudio.py` | `nerfstudio` |
| Day05 | 🔧 Build + Milvus | Production Schema Design | `Day05_production_schema_design.py` | `pymilvus numpy scikit-learn` |
| Day05 | 🗜️ Compression | Pruning Hands-on | `Day05_pruning_hands_on.py` | `torch torchvision datasets pillow` |
| Day06 | 🔧 Build + Milvus | Scene Retrieval Service | `Day06_scene_retrieval_service.py` | `pymilvus numpy scikit-learn` |
| Day07 | 🛠️ Hands-on | Fine-tune YOLOv8 on YCB Dataset | `Day07_fine_tune_yolov8_on_ycb_dataset.py` | `ultralytics pytest` |
| Day07 | 🔧 Build + Milvus | Detection Embedding Store | `Day07_detection_embedding_store.py` | `pymilvus numpy scikit-learn` |
| Day07 | 🗜️ Compression | Distillation Hands-on | `Day07_distillation_hands_on.py` | `torch torchvision datasets pillow` |
| Day08 | 🛠️ Hands-on | Run Depth Anything v2 + Point Cloud | `Day08_run_depth_anything_v2_point_cloud.py` | `transformers datasets pillow` |
| Day08 | 🔧 Build + Milvus | Multi-modal (RGB + Depth) | `Day08_multi_modal_rgb_depth.py` | `pymilvus numpy scikit-learn` |
| Day08 | 🗜️ Compression | ONNX Export | `Day08_onnx_export.py` | `onnxruntime torch torchvision datasets numpy pillow` |
| Day09 | 🛠️ Hands-on | Run MegaPose on YCB Object | `Day09_run_megapose_on_ycb_object.py` | `# clone the pose repo (see resources)` |
| Day09 | 🔧 Build + Milvus | Object Pose Library | `Day09_object_pose_library.py` | `pymilvus numpy scikit-learn` |
| Day09 | 🗜️ Compression | TensorRT Basics | `Day09_tensorrt_basics.py` | `onnxruntime torch torchvision datasets numpy pillow` |
| Day10 | 🛠️ Hands-on | Run AnyGrasp on Point Cloud | `Day10_run_anygrasp_on_point_cloud.py` | `# clone the grasp repo (see resources)` |
| Day10 | 🔧 Build + Milvus | Grasp Pose Library | `Day10_grasp_pose_library.py` | `pymilvus numpy scikit-learn` |
| Day10 | 🗜️ Compression | TensorRT FP16 | `Day10_tensorrt_fp16.py` | `onnxruntime torch torchvision datasets numpy pillow` |
| Day11 | 🛠️ Hands-on | Run ORB-SLAM3 on TUM RGB-D | `Day11_run_orb_slam3_on_tum_rgb_d.py` | `# mostly C++ (ORB-SLAM3)` |
| Day11 | 🔧 Build + Milvus | Semantic SLAM Map | `Day11_semantic_slam_map.py` | `pymilvus numpy scikit-learn` |
| Day11 | 🗜️ Compression | TensorRT INT8 | `Day11_tensorrt_int8.py` | `onnxruntime torch torchvision datasets numpy pillow` |
| Day12 | 🔧 Build + Milvus | Pipeline + Milvus Integration | `Day12_pipeline_milvus_integration.py` | `pymilvus numpy scikit-learn` |
| Day12 | 🗜️ Compression | Benchmark Table | `Day12_benchmark_table.py` | `torch torchvision datasets pillow` |
| Day13 | 🛠️ Hands-on | Load & Run a VLA (SmolVLA-first) | `Day13_load_run_a_vla_smolvla_first.py` | `lerobot transformers numpy` |
| Day13 | 🔧 Build + Milvus | Retrieval-Augmented VLA | `Day13_retrieval_augmented_vla.py` | `pymilvus numpy scikit-learn` |
| Day13 | 🗜️ Compression | Attention Head Pruning | `Day13_attention_head_pruning.py` | `torch` |
| Day14 | 🛠️ Hands-on | Fine-tune a VLA (SmolVLA) with LoRA | `Day14_fine_tune_a_vla_smolvla_with_lora.py` | `lerobot transformers peft` |
| Day14 | 🔧 Build + Milvus | Demo Replay Buffer | `Day14_demo_replay_buffer.py` | `pymilvus numpy scikit-learn` |
| Day14 | 🗜️ Compression | LoRA + QLoRA | `Day14_lora_qlora.py` | `torch` |
| Day15 | 🛠️ Hands-on | Load & Amplify Demo Episodes | `Day15_load_amplify_demo_episodes.py` | `lerobot numpy` |
| Day15 | 🔧 Build + Milvus | Demo-Episode Deduplication | `Day15_demo_episode_deduplication.py` | `pymilvus numpy scikit-learn` |
| Day15 | 🗜️ Compression | Low-rank Factorisation | `Day15_low_rank_factorisation.py` | `torch` |
| Day16 | 🔧 Build + Milvus | Demo-Episode Browser | `Day16_demo_episode_browser.py` | `pymilvus numpy scikit-learn` |
| Day17 | 🛠️ Hands-on | Depth-conditioned ControlNet Augmentation | `Day17_depth_conditioned_controlnet_augmentation.py` | `diffusers transformers accelerate datasets pillow` |
| Day17 | 🔧 Build + Milvus | Diversity-guided Augmentation | `Day17_diversity_guided_augmentation.py` | `pymilvus numpy scikit-learn` |
| Day18 | 🛠️ Hands-on | Run DreamerV3 | `Day18_run_dreamerv3.py` | `# clone DreamerV3 (see resources)` |
| Day18 | 🔧 Build + Milvus | World Model State Memory | `Day18_world_model_state_memory.py` | `pymilvus numpy scikit-learn` |
| Day18 | 🗜️ Compression | Flash Attention & Speculative Decoding | `Day18_flash_attention_speculative_decoding.py` | `torch` |
| Day19 | 🛠️ Hands-on | 3DGS Scene + Grasp Poses | `Day19_3dgs_scene_grasp_poses.py` | `nerfstudio` |
| Day19 | 🔧 Build + Milvus | 3DGS Object Index | `Day19_3dgs_object_index.py` | `pymilvus numpy scikit-learn` |
| Day19 | 🗜️ Compression | 4-bit Quantisation (GPTQ/AWQ) | `Day19_4_bit_quantisation_gptq_awq.py` | `torch` |
| Day20 | 🗜️ Compression | Compress the Pipeline | `Day20_compress_the_pipeline.py` | `torch torchvision datasets pillow` |
| Day21 | 🛠️ Hands-on | Implement Attention from Scratch | `Day21_implement_attention_from_scratch.py` | `torch numpy` |
| Day21 | 🔧 Build + Milvus | ANN Benchmarking | `Day21_ann_benchmarking.py` | `pymilvus numpy scikit-learn` |
| Day21 | 🗜️ Compression | Speculative Decoding Hands-on | `Day21_speculative_decoding_hands_on.py` | `` |
| Day22 | 🛠️ Hands-on | Add Latency Profiler | `Day22_add_latency_profiler.py` | `` |
| Day23 | 🛠️ Hands-on | Custom PyTorch Dataset | `Day23_custom_pytorch_dataset.py` | `torch` |
| Day23 | 🔧 Build + Milvus | Anomaly Detection | `Day23_anomaly_detection.py` | `pymilvus numpy scikit-learn` |
| Day29 | 🗜️ Compression | Final Benchmark | `Day29_final_benchmark.py` | `torch torchvision datasets pillow` |
