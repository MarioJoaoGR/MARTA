
import pytest
from httpie.cli.dicts import HTTPHeadersDict
from unittest.mock import patch

def test_invalid_input():
    headers = HTTPHeadersDict()
    
    # Adding a valid header pair
    headers.add('Content-Type', 'application/json')
    
    # Attempting to remove an invalid key (non-existent key)
    with pytest.raises(KeyError):
        headers.remove_item('Invalid-Key', 'value')
    
    # Adding a valid header pair
    headers.add('Set-Cookie', 'cookie1=value1;')
    
    # Attempting to remove an invalid value (non-existent value)
    with pytest.raises(ValueError):
        headers.remove_item('Set-Cookie', 'invalid_value')
    
    # Adding a valid header pair
    headers.add('Cache-Control', None)
    
    # Attempting to remove the header with an invalid value (None)
    with pytest.raises(ValueError):
        headers.remove_item('Cache-Control', 'invalid_value')
