from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/bwkrayb/eink-running-display.git",
        entrypoint="month-stats.py:monthly_stats",
    ).deploy(
        name="monthly-running",
        work_pool_name="my-managed-pool",
        cron="0 12,21 * * *",
    )
