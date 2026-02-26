"""Scores and ranks filtered stories."""


def score_story(story: dict) -> float:
    """Calculate a relevance score for a single story.

    Scoring should consider at minimum:
    - story score (upvotes)
    - number of comments
    - recency (time field is a Unix timestamp)

    Args:
        story: Story dictionary from the HN API.

    Returns:
        A float representing the story's relevance score.

    TODO: implement this function.
    """
    raise NotImplementedError


def rank_stories(stories: list[dict]) -> list[dict]:
    """Sort stories by their computed score, descending.

    Args:
        stories: List of filtered story dictionaries.

    Returns:
        Stories sorted from highest to lowest score.

    TODO: implement this function using score_story().
    """
    raise NotImplementedError