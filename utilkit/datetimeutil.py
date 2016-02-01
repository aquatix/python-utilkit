"""
datetime helper functions, from formatting to timezone magic and more
"""
import datetime
from time import mktime
from pytz.tzinfo import StaticTzInfo


# Formatting

def unix_to_string(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')


def unix_to_python(timestamp):
    """
    Convert unix timestamp to python datetime
    """
    # Not sure how correct this is to do here, but return 'null' if the timestamp from Pocket is 0
    if int(timestamp) == 0:
        return None
    else:
        return datetime.datetime.utcfromtimestamp(float(timestamp))


def datetime_to_string(timestamp):
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')


# Timezone helpers

def is_dst(zonename):
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
