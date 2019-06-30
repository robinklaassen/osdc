# OpenSky Data Collector

The `osdc` Python package collects selected data from the 
[Opensky API](https://opensky-network.org/apidoc/)
and stores it in an [Influx](https://www.influxdata.com/) database.

## Installation

First install the `opensky_api` package by hand
(since it's not on PyPI and PEP 508 sucks for dependencies):

```sh
pip install git+https://github.com/openskynetwork/opensky-api.git@master#egg=opensky_api&subdirectory=python
```

Then install this package:

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