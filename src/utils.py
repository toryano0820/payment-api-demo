from datetime import datetime, timedelta
import re


def parse_datetime(str_datetime: str):
    patterns = [
        r'%Y-%m-%dT%H:%M:%S.%fZ',
        r'%Y-%m-%dT%H:%M:%SZ',
        r'%Y-%m-%d',
        r'%Y-%m-%d'
    ]
    short_patterns = [
        r'%m/%y',
        r'%m-%y',
        r'%m%y'
    ]

    for pattern in patterns:
        try:
            return datetime.strptime(str_datetime, pattern)
        except ValueError:
            pass

    for pattern in short_patterns:
        try:
            dt = datetime.strptime(str_datetime, pattern)
            dt += timedelta(31)
            return dt - timedelta(days=dt.day)
        except ValueError:
            pass

    return None
