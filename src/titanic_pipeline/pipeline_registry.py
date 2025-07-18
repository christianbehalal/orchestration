"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from titanic_pipeline.pipelines import training as tr  # ✅ Ajout de l'import

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = {
        "training": tr.create_pipeline(),  # ✅ Enregistrement explicite du pipeline
    }
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
