"""Filters stories by keywords and minimum score."""

DEFAULT_KEYWORDS = [
    "data engineering",
    "data pipeline",
    "airflow",
    "dbt",
    "python",
    "sql",
    "kubernetes",
    "docker",
    "machine learning",
    "analytics",
    "ai agents",
    "agentic",
]


def matches_keywords(story: dict, keywords: list[str]) -> bool:
    """Check if a story title contains any of the given keywords.

    Args:
        story: Story dictionary with at least a 'title' field.
        keywords: List of keywords to match against (case-insensitive).

    Returns:
        True if the story title contains at least one keyword.
    """
    title = story.get("title", "").lower()
    return any(keyword.lower() in title for keyword in keywords)


def filter_stories(
    stories: list[dict],
    keywords: list[str] = DEFAULT_KEYWORDS,
    min_score: int = 10,
) -> list[dict]:
    """Filter stories by keyword match and minimum score.

    Args:
        stories: List of story dictionaries from the HN API.
        keywords: Keywords to filter by. Defaults to DEFAULT_KEYWORDS.
        min_score: Minimum score threshold. Defaults to 10.

    Returns:
        Filtered list of stories matching at least one keyword and min score.
    """
    return [
        story
        for story in stories
        if matches_keywords(story, keywords) and story.get("score", 0) >= min_score
    ]
