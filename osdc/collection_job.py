import logging

from influxdb import InfluxDBClient

from osdc.mapper import map_to_points
from osdc.opensky_service import OpenskyService

_logger = logging.getLogger(__name__)


def run(oss: OpenskyService, client: InfluxDBClient):
    """
    Run a single retrieval of OpenSky data and writes results to InfluxDB.
    :return: None.
    """

    result: dict = oss.get_current_states(bounding_box=())

    if result is None:
        _logger.warning("No data retrieved from OpenSky, skipping collection")
        return

    points = map_to_points(result)
    client.write_points(points)
