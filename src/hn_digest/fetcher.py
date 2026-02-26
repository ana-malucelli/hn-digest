"""Fetches top stories from the Hacker News API."""

import requests

HN_API_BASE = "https://hacker-news.firebaseio.com/v0"
TOP_STORIES_URL = f"{HN_API_BASE}/topstories.json"
ITEM_URL = f"{HN_API_BASE}/item/{{item_id}}.json"


def fetch_top_story_ids(limit: int = 100) -> list[int]:
    """Fetch IDs of the top stories from Hacker News.

    Args:
        limit: Maximum number of story IDs to return.

    Returns:
        List of story IDs, capped at limit.

    Raises:
        requests.HTTPError: If the API request fails.
    """
    response = requests.get(TOP_STORIES_URL, timeout=10)
    response.raise_for_status()
    return response.json()[:limit]


def fetch_story(story_id: int) -> dict:
    """Fetch a single story by ID from Hacker News.

    Args:
        story_id: The Hacker News item ID.

    Returns:
        Story data as a dictionary.

    Raises:
        requests.HTTPError: If the API request fails.
    """
    response = requests.get(ITEM_URL.format(item_id=story_id), timeout=10)
    response.raise_for_status()
    return response.json()


def fetch_stories(limit: int = 100) -> list[dict]:
    """Fetch full story data for the top N stories.

    Args:
        limit: Number of top stories to fetch.

    Returns:
        List of story dictionaries.
    """
    story_ids = fetch_top_story_ids(limit)
    stories = []
    for story_id in story_ids:
        story = fetch_story(story_id)
        if story and story.get("type") == "story":
            stories.append(story)
    return stories
