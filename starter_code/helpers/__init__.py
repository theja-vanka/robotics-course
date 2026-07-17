"""
Shared helpers for the starter exercises.

Every DayXX/ starter file imports the *common* setup from this package instead of
copy-pasting it, so there is exactly one place to fix if a dataset, model, or Milvus
detail changes:

    helpers.runtime      DEVICE (cuda -> mps -> cpu)
    helpers.datasets     read robot-scene frames from the LeRobot video datasets
    helpers.embeddings   CLIP / DINOv2 vectors of those frames (cached to .npy)
    helpers.milvus       fresh_client()  — a clean, file-based Milvus (no Docker)
    helpers.compress     example_input(), measure(), log_metrics()  — compression bench
    helpers.images       load_scene_image()  — one PIL frame for the vision hands-ons

Nothing here needs filling in — these are the "provided" parts of each exercise.
"""
