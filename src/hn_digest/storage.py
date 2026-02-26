"""Saves digest output to disk and handles deduplication across runs."""

import json
from datetime import date
from pathlib import Path

OUTPUT_DIR = Path("output")


def load_seen_ids(seen_ids_path: Path) -> set[int]:
    """Load previously seen story IDs from a JSON file.

    Args:
        seen_ids_path: Path to the JSON file storing seen IDs.

    Returns:
        Set of story IDs already processed in previous runs.

    TODO: implement this function.
    Hint: file may not exist on the first run — handle that case.
    """
    raise NotImplementedError


def save_seen_ids(seen_ids: set[int], seen_ids_path: Path) -> None:
    """Persist the updated set of seen story IDs to disk.

    Args:
        seen_ids: Updated set of all seen story IDs.
        seen_ids_path: Path to the JSON file to write.

    TODO: implement this function.
    """
    raise NotImplementedError


def deduplicate(stories: list[dict], seen_ids: set[int]) -> list[dict]:
    """Remove stories that have already been seen in previous runs.

    Args:
        stories: List of scored and ranked story dictionaries.
        seen_ids: Set of story IDs already processed.

    Returns:
        Only stories whose IDs are not in seen_ids.

    TODO: implement this function.
    """
    raise NotImplementedError


def save_digest(stories: list[dict], output_dir: Path = OUTPUT_DIR) -> Path:
    """Save the daily digest as a JSON file named by today's date.

    Args:
        stories: Final list of stories to save.
        output_dir: Directory to write the output file into.

    Returns:
        Path to the written file.

    TODO: implement this function.
    Hint: filename should follow the pattern YYYY-MM-DD.json
    """
    raise NotImplementedError
