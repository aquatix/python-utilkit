"""
String/unicode helper functions
"""
import math, string

def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)  # noqa for undefined-variable
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        try:
            return unicode(ascii_text)  # noqa for undefined-variable
        except NameError:
            # This is Python 3, just return the obj as it's already unicode
            return obj
    except NameError:
        # This is Python 3, just return the obj as it's already unicode
        return obj


def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        try:
            return unicode(obj).encode('unicode_escape')  # noqa for undefined-variable
        except NameError:
            # This is Python 3, just return the obj as it's already unicode
            return obj


def range_bytes():
    return range(256)
def range_printable():
    return (ord(c) for c in string.printable)
def shannon_entropy(data, iterator=range_bytes):
    """
    Calculate Shannon entropy of a given string `data`
    Example: shannon_entropy('gargleblaster', range_printable)

    Stolen from Ero Carrera
    http://blog.dkbza.org/2007/05/scanning-data-for-entropy-anomalies.html
    http://pythonfiddle.com/shannon-entropy-calculation/
    """
    if not data:
        return 0
    entropy = 0
    for x in iterator():
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy
