"""Tests for the filter module."""

import pytest
from hn_digest.filter import filter_stories, matches_keywords


# ── matches_keywords ──────────────────────────────────────────────────────────

def test_matches_keywords_returns_true_when_keyword_found():
    story = {"title": "Building data pipelines with Python"}
    assert matches_keywords(story, ["data pipeline"]) is True


def test_matches_keywords_is_case_insensitive():
    story = {"title": "Getting started with AIRFLOW"}
    assert matches_keywords(story, ["airflow"]) is True


def test_matches_keywords_returns_false_when_no_match():
    story = {"title": "How to grow tomatoes at home"}
    assert matches_keywords(story, ["python", "dbt"]) is False


def test_matches_keywords_handles_missing_title():
    story = {}
    assert matches_keywords(story, ["python"]) is False


# ── filter_stories ────────────────────────────────────────────────────────────

def test_filter_stories_removes_low_score_stories():
    stories = [
        {"title": "Python tutorial", "score": 5},
        {"title": "Python tutorial", "score": 50},
    ]
    result = filter_stories(stories, keywords=["python"], min_score=10)
    assert len(result) == 1
    assert result[0]["score"] == 50


def test_filter_stories_removes_non_matching_stories():
    stories = [
        {"title": "How to cook pasta", "score": 100},
        {"title": "dbt best practices", "score": 100},
    ]
    result = filter_stories(stories, keywords=["dbt"], min_score=1)
    assert len(result) == 1
    assert "dbt" in result[0]["title"]


def test_filter_stories_returns_empty_when_nothing_matches():
    stories = [{"title": "Celebrity gossip", "score": 500}]
    result = filter_stories(stories, keywords=["python"], min_score=10)
    assert result == []


# ── TODO: add your own tests below ───────────────────────────────────────────
# Ideas:
# - test that ai agents keyword matches correctly
# - test filter_stories with an empty input list
# - test filter_stories when all stories match