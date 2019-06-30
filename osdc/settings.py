import conf

LOG_LEVEL = conf.get('log_level', 'INFO').upper()

INFLUXDB_HOST = conf.get('influxdb_host', 'localhost')
INFLUXDB_PORT = conf.get('influxdb_port', 8086)
INFLUXDB_USERNAME = conf.get('influxdb_username', 'root')
INFLUXDB_PASSWORD = conf.get('influxdb_password', 'root')
INFLUXDB_DATABASE = conf.get('influxdb_database', 'hot_ginger')
INFLUXDB_MEASUREMENT = conf.get('influxdb_measurement', 'opensky')

OPENSKY_USE_AUTH = conf.get('opensky_use_auth', "false").lower() == "true"
OPENSKY_USERNAME = conf.get('opensky_username')
OPENSKY_PASSWORD = conf.get('opensky_password')

COLLECT_EVERY_SEC = conf.get('collect_every_sec', 5)

RETENTION_NAME = conf.get('retention_name', 'minimal')
RETENTION_DURATION = conf.get('retention_duration', '1h')
RETENTION_REPLICATION = conf.get('retention_replication', 1)
