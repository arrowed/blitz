__author__="ghermeto"
__date__ ="$28/07/2011 19:13:12$"

import re
from urllib.parse import urlparse

def validate_url(url):
    parsed = urlparse(url)
    return parsed.scheme and parsed.netloc

def validate_int(value):
    str_value = str(value)
    return True if re.search("^[0-9]+$", str_value) else False

def validate_list(lst):
    return isinstance(lst, list) or isinstance(lst, tuple)

def validate(options):
    failed = []
    if 'referrer' in options and not validate_url(options['referrer']):
        failed.append('referrer')
    if 'status' in options and not validate_int(options['status']):
        failed.append('status')
    if 'timeout' in options and not validate_int(options['timeout']):
        failed.append('timeout')
    if 'cookies' in options and not validate_list(options['cookies']):
        failed.append('cookies')
    if 'headers' in options and not validate_list(options['headers']):
        failed.append('headers')
    return failed
        