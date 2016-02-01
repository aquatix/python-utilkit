import datetime
from time import mktime

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


