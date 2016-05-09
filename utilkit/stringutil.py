"""
String/unicode helper functions
"""

def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)  # pylint:disable=undefined-variable
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)  # pylint:disable=undefined-variable

def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')  # pylint:disable=undefined-variable
