# OpenSky Data Collector

The `osdc` Python package collects selected data from the Opensky API
and stores it in an Influx database.

## Installation

After installing the `opensky_api` package by hand (since it's not on PyPI)
, run:

```sh
pip install .
```

## Configuring and starting

Start the collector using default configuration:

```sh
python -m osdc
```

To customize configuration, create a `config.yml` file and run:

```sh
python -m osdc --config config.yml
```

Have a look at the `settings.py` file to see what can be configured.