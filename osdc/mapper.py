from datetime import datetime


def map_to_points(result: dict) -> list:
    ts: datetime = result.get('timestamp')
    states: list = result.get('states')

    points = [_make_influx_object(state, ts) for state in states
              if state.get('latitude') is not None]
    return points


def _make_influx_object(state: dict, ts: datetime):

    return {
        "measurement": "opensky",
        "tags": {
            "icao24": state.get('icao24'),
            "on_ground": state.get('on_ground')
        },
        "time": str(ts),
        "fields": {
            "lat": float(state.get('latitude')),
            "lon": float(state.get('longitude'))
        }
    }
