import uuid
import time
from google.cloud import bigquery


def wait_for_job(job):
    while True:
        job.reload()  # Refreshes the state via a GET request.
        if job.state == 'DONE':
            if job.error_result:
                raise RuntimeError(job.errors)
            return
        time.sleep(1)

bigquery_client = bigquery.Client()
query = "SELECT * FROM [bigquery-public-data:github_repos.sample_files] WHERE lower(RIGHT(path, 3)) = '.py' limit 10 "
client = bigquery.Client()
query_job = client.run_async_query(str(uuid.uuid4()), query)
query_job.use_legacy_sql = True
query_job.begin()
wait_for_job(query_job)

# Drain the query results by requesting a page at a time.
query_results = query_job.results()
page_token = None

while True:
    rows, total_rows, page_token = query_results.fetch_data(
        max_results=10,
        page_token=page_token)

    for row in rows:
        print(row)

    if not page_token:
        break
