
import pytest
from unittest.mock import patch
from httpie.cli.dicts import HTTPHeadersDict

def test_invalid_input():
    headers = HTTPHeadersDict()
    
    # Test adding a header with None value, it should set the value to None and remove any previous None values
    headers.add('Content-Type', 'application/json')
    assert headers['Content-Type'] == 'application/json'
    
    headers.add('Set-Cookie', 'cookie1=value1;')
    assert headers['Set-Cookie'] == 'cookie1=value1;'
    
    headers.add('Cache-Control', None)
    assert headers['Cache-Control'] is None
    
    # Test adding a header with None value, it should overwrite any existing None values and set the new value to None
    headers.add('Cache-Control', 'no-cache')
    assert headers['Cache-Control'] == 'no-cache'
