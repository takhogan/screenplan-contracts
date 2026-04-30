"""Canonical ScreenPlan JSON Schemas, shipped as package data.

This package contains *only* the schema JSON files; ``screenplan-contracts``
(Pydantic models + validators) depends on it and reads schemas via
``importlib.resources.files('screenplan_contracts_schemas.schemas')``.

PyInstaller / cx_Freeze: the JSON files are real package data, so frozen
builds bundle them automatically.
"""

from importlib import resources
from typing import Iterable

__all__ = ["schema_text", "list_schemas"]


def schema_text(name: str) -> str:
    """Return the raw JSON text of a packaged schema, e.g. 'script.schema.json'."""
    return resources.files(__name__).joinpath("schemas", name).read_text("utf-8")


def list_schemas() -> Iterable[str]:
    """Yield filenames of all packaged JSON Schema documents (``*.schema.json``).

    Mirrors the TypeScript ``listSchemas()`` helper in @screenplan/contracts.
    Companion data files (e.g. ``script-action-artifacts.json``) are excluded —
    use ``schema_text(name)`` directly to read those.
    """
    for entry in resources.files(__name__).joinpath("schemas").iterdir():
        if entry.name.endswith(".schema.json"):
            yield entry.name
