import pytest
from datetime import datetime

from utils import parse_datetime


def test_datetime_formats():
    datetime_samples = [
        '2022-01-31T00:00:00.000Z',
        '2022-01-31T00:00:00Z',
        '2022-01-31',
        '01/22',
        '01-22',
        '0122'
    ]
    for sample in datetime_samples:
        assert isinstance(parse_datetime(sample), datetime)
