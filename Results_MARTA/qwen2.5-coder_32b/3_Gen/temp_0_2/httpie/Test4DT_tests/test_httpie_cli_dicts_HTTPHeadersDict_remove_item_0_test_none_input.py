
import pytest
from httpie.cli.dicts import HTTPHeadersDict

def test_none_input():
    headers = HTTPHeadersDict()
    
    # Add a header with a value
    headers.add('Content-Type', 'application/json')
    
    # Remove the header with None value
    with pytest.raises(ValueError):
        headers.remove_item('Content-Type', None)
