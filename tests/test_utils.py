
import os
import pytest
import sys
from datetime import datetime, timedelta

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src/payment_api'))

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
