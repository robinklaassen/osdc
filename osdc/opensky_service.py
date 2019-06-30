import logging
from datetime import datetime, timezone
from typing import Optional, Tuple

import requests
from opensky_api import OpenSkyApi, OpenSkyStates

from osdc.settings import OPENSKY_USE_AUTH, OPENSKY_USERNAME, OPENSKY_PASSWORD


class OpenskyService:
    """
    Service layer around the OpenSky Network API.

    Data is fetched based on bounding box, a tuple (min_lat, max_lat, min_lon, max_lon)

    # Useful bounding boxes per country: https://gist.github.com/graydon/11198540
    dict({
        "world": (),
        "europe": (33.7, 71.9, -27.2, 44.2),
        "netherlands": (50.80, 53.51, 3.31, 7.09)
    })
    """

    _logger: logging.Logger
    _api: OpenSkyApi

    def __init__(self):
        self._logger = logging.getLogger(__name__)

        # Initialize API
        if OPENSKY_USE_AUTH:
            self._logger.info("Using basic authentication for Opensky")
            self._api = OpenSkyApi(username=OPENSKY_USERNAME,
                                   password=OPENSKY_PASSWORD)
        else:
            self._logger.info("Using Opensky anonymously")
            self._api = OpenSkyApi()

    def get_current_states(self, bounding_box: Tuple = None) -> Optional[dict]:

        if bounding_box is None:
            self._logger.warning("No bounding box given for opensky data, defaulting to 'world'")
            bounding_box = ()
        else:
            self._logger.debug("Bounding box for opensky request is: %s", bounding_box)

        try:
            s: Optional[OpenSkyStates] = self._api.get_states(bbox=bounding_box)
        except requests.exceptions.ReadTimeout:
            self._logger.warning("Call to OpenSky timed out")
            return None

        if s is not None:
            timestamp = datetime.fromtimestamp(s.time, timezone.utc)
            self._logger.debug("Retrieved %s records for timestamp %s",
                               len(s.states),
                               timestamp)

            return dict(timestamp=timestamp, states=list(map(lambda x: vars(x), s.states)))
        else:
            self._logger.warning("No records retrieved from Opensky")
            return None
