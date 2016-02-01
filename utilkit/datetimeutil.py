"""
datetime helper functions, from formatting to timezone magic and more
"""
from datetime import datetime, timedelta
from time import mktime
from pytz.tzinfo import StaticTzInfo
import pytz


# Formatting

def unix_to_string(timestamp, dt_format='%Y-%m-%d %H:%M:%S'):
    return datetime.fromtimestamp(int(timestamp)).strftime(dt_format)


def unix_to_python(timestamp):
    """
    Convert unix timestamp to python datetime
    """
    # Not sure how correct this is to do here, but return 'null' if the timestamp from Pocket is 0
    if int(timestamp) == 0:
        return None
    else:
        return datetime.utcfromtimestamp(float(timestamp))


def datetime_to_string(timestamp, dt_format='%Y-%m-%d %H:%M:%S'):
    """
    Format datetime object to string
    """
    return timestamp.strftime(dt_format)


def simple_time(value):
    """
    Format a datetime or timedelta object to a string of format HH:MM
    """
    if isinstance(value, timedelta):
        return ':'.join(str(value).split(':')[:2])
    return datetime_to_string(value, '%H:%M')


# Timezone helpers

def is_dst(zonename):
    """
    Find out whether it's Daylight Saving Time in this timezone
    """
    tz = pytz.timezone(zonename)
    now = pytz.utc.localize(datetime.utcnow())
    return now.astimezone(tz).dst() != timedelta(0)


class OffsetTime(StaticTzInfo):
    """
    A dumb timezone based on offset such as +0530, -0600, etc.
    """
    def __init__(self, offset):
        hours = int(offset[:3])
        minutes = int(offset[0] + offset[3:])
        self._utcoffset = timedelta(hours=hours, minutes=minutes)


def load_datetime(value, dt_format):
    """
    Create timezone-aware datetime object
    """
    if dt_format.endswith('%z'):
        dt_format = dt_format[:-2]
        offset = value[-5:]
        value = value[:-5]
        if offset != offset.replace(':', ''):
            # strip : from HHMM if needed (isoformat() adds it between HH and MM)
            offset = '+' + offset.replace(':', '')
            value = value[:-1]
        return OffsetTime(offset).localize(datetime.strptime(value, dt_format))

    return datetime.strptime(value, dt_format)
