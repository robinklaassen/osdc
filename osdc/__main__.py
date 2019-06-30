import logging
import sys

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from osdc import influx_client, collection_job, settings
from osdc.opensky_service import OpenskyService

from osdc.settings import COLLECT_EVERY_SEC


def main():
    # Configure logging
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format='%(asctime)s - %(levelname)s | %(message)s',
        handlers=(logging.StreamHandler(sys.stdout),))

    # Instantiate OpenSky service
    oss = OpenskyService()

    # Create InfluxDB client
    client = influx_client.create_client()

    # Start scheduled collection job
    sched = BlockingScheduler()
    sched.add_job(collection_job.run, args=[oss, client], trigger=CronTrigger(second=f"*/{COLLECT_EVERY_SEC}"))
    sched.start()


if __name__ == "__main__":
    main()
