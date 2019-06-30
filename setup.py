"""This is the installation toolset for this project."""
from datetime import datetime
from pathlib import Path
from subprocess import Popen, PIPE
from setuptools import setup, find_packages


with open('README.md', 'r') as fh:
    long_description = fh.read()


def _build_time():
    ctime = datetime.utcnow()
    return ctime.strftime('%Y%m%d.%H%M%S')


def _revision():
    cwd = str(Path(__file__).parent.absolute())
    with Popen('git rev-parse --short HEAD', shell=True, stdout=PIPE, cwd=cwd) as proc:
        outb, errb = proc.communicate()
        result = outb.decode('utf8').strip()
    return result or 'nogit'


setup(
    name='osdc',
    version=f'{_build_time()}-{_revision()}',
    description='The OpenSky Data Collector',
    long_description=long_description,
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'dataclasses;python_version<"3.7"',
        'conf',
        'opensky_api',
        'influxdb',
        'requests',
        'apscheduler',
    ],
    tests_require=[
        'wheel',
        'setuptools',
        'pylint',
        'coverage',
        'pytest',
        'mock',
    ],
    entry_points={
        'console_scripts': [
            'osdc = osdc.__main__:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: ALL RIGHTS RESERVED.',
        'Operating System :: POSIX :: Linux',
    ],
)
