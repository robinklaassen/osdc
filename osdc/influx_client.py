import logging

import requests
from influxdb.client import InfluxDBClient

from osdc.settings import (INFLUXDB_HOST,
                           INFLUXDB_PORT,
                           INFLUXDB_USERNAME,
                           INFLUXDB_PASSWORD,
                           INFLUXDB_DATABASE, RETENTION_NAME, RETENTION_DURATION, RETENTION_REPLICATION)

_logger = logging.getLogger(__name__)


def create_client() -> InfluxDBClient:
    client = InfluxDBClient(
        host=INFLUXDB_HOST,
        port=INFLUXDB_PORT,
        username=INFLUXDB_USERNAME,
        password=INFLUXDB_PASSWORD,
        database=INFLUXDB_DATABASE
    )

    # Test connection
    try:
        client.ping()
    except requests.exceptions.ConnectionError:
        _logger.error('Connection to InfluxDB was refused!')
        exit(code=1)  # TODO replace with backoff retry

    # Create database (will pass if already exists)
    client.create_database(INFLUXDB_DATABASE)

    # Set retention policy on database
    client.create_retention_policy(name=RETENTION_NAME,
                                   duration=RETENTION_DURATION,
                                   replication=RETENTION_REPLICATION,
                                   database=INFLUXDB_DATABASE,
                                   default=True)

    _logger.info("InfluxDB client created successfully")

    return client
