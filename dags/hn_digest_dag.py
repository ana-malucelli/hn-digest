"""Airflow DAG for the daily Hacker News digest pipeline."""

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

# TODO: import your functions from hn_digest once implemented
# from hn_digest.fetcher import fetch_stories
# from hn_digest.filter import filter_stories
# from hn_digest.scorer import rank_stories
# from hn_digest.storage import load_seen_ids, save_seen_ids, deduplicate, save_digest


with DAG(
    dag_id="hn_digest",
    description="Fetch, filter, score and save daily Hacker News stories",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["hn", "digest"],
) as dag:

    # TODO: replace each placeholder callable with your real functions

    fetch_task = PythonOperator(
        task_id="fetch_stories",
        python_callable=lambda: None,  # TODO: replace with fetch_stories
    )

    filter_task = PythonOperator(
        task_id="filter_stories",
        python_callable=lambda: None,  # TODO: replace with filter_stories
    )

    score_task = PythonOperator(
        task_id="rank_stories",
        python_callable=lambda: None,  # TODO: replace with rank_stories
    )

    save_task = PythonOperator(
        task_id="save_digest",
        python_callable=lambda: None,  # TODO: replace with save_digest
    )

    # Task dependencies — this is the pipeline order, do not change
    fetch_task >> filter_task >> score_task >> save_task
