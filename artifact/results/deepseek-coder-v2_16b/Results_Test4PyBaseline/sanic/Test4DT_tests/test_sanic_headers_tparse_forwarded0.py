# Module: sanic.headers
import pytest
from typing import Optional, List, Tuple
from sanic.headers import parse_forwarded
from collections import namedtuple

# Assuming Config and MultiDict are defined elsewhere in the module or imported from a library
Config = namedtuple('Config', ['FORWARDED_SECRET'])
MultiDict = dict
Options = dict

def test_parse_forwarded_no_header():
    headers = MultiDict()
    config = Config(FORWARDED_SECRET='secret')
    assert parse_forwarded(headers, config) is None

def test_parse_forwarded_invalid_secret():
    headers = MultiDict({'Forwarded': 'by=192.168.1.1; for=example.com'})
    config = Config(FORWARDED_SECRET='wrongsecret')
    assert parse_forwarded(headers, config) is None

def test_parse_forwarded_valid_header():
    headers = MultiDict({'Forwarded': 'by=ExampleHost; secret=mysecret; host=EXAMPLE.com; proto=HTTP/1.1; port=8080; path=https://example.org/page'})
    config = Config(FORWARDED_SECRET='mysecret')
    expected_output = {
        'by': 'examplehost',
        'for': '',
        'host': 'example.com',
        'proto': 'http/1.1',
        'port': 8080,
        'path': 'https://example.org/page'
    }
    assert parse_forwarded(headers, config) == expected_output
