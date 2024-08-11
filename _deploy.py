from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/bwkrayb/eink-running-display.git",
        entrypoint="month-stats.py:monthly_stats",
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-managed-pool",
        cron="8 1 * * *",
    )
