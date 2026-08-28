# Module: ansible.galaxy.api
# test_ansible_galaxy_api.py
import pytest
from ansible.galaxy.apiclass import GalaxyError
from unittest.mock import MagicMock
import requests
import json

@pytest.fixture
def http_error():
    response = MagicMock()
    response.code = 404
    response.geturl.return_value = 'http://example.com/api'
    response.read.return_value = json.dumps({'message': 'Not Found', 'code': 'E404'})
    return response

def test_GalaxyError_with_v2_endpoint(http_error):
    with pytest.raises(GalaxyError) as excinfo:
        raise GalaxyError(http_error, "An error occurred while trying to access the Galaxy API.")
    
    assert str(excinfo.value) == "An error occurred while trying to access the Galaxy API. (HTTP Code: 404, Message: Not Found Code: E404)"

def test_GalaxyError_with_v3_endpoint(http_error):
    http_error.geturl.return_value = 'http://example.com/api/v3'
    http_error.read.return_value = json.dumps({'errors': [{'detail': 'Not Found', 'code': 'E404'}]})
    
    with pytest.raises(GalaxyError) as excinfo:
        raise GalaxyError(http_error, "An error occurred while trying to access the Galaxy API.")
    
    assert str(excinfo.value) == "An error occurred while trying to access the Galaxy API. (HTTP Code: 404, Message: Not Found Code: E404)"

def test_GalaxyError_with_unknown_endpoint(http_error):
    http_error.geturl.return_value = 'http://example.com/api/v1'
    http_error.read.return_value = json.dumps({'default': 'Not Found'})
    
    with pytest.raises(GalaxyError) as excinfo:
        raise GalaxyError(http_error, "An error occurred while trying to access the Galaxy API.")
    
    assert str(excinfo.value) == "An error occurred while trying to access the Galaxy API. (HTTP Code: 404, Message: Not Found)"

def test_GalaxyError_with_invalid_http_error():
    http_error = MagicMock()
    http_error.code = 404
    http_error.geturl.return_value = 'http://example.com/api'
    http_error.read.side_effect = Exception("Read error")
    
    with pytest.raises(GalaxyError) as excinfo:
        raise GalaxyError(http_error, "An error occurred while trying to access the Galaxy API.")
    
    assert str(excinfo.value) == "An error occurred while trying to access the Galaxy API. (HTTP Code: 404, Message: Not Found)"

def test_GalaxyError_with_invalid_json():
    http_error = MagicMock()
    http_error.code = 404
    http_error.geturl.return_value = 'http://example.com/api'
    http_error.read.return_value = "Invalid JSON"
    
    with pytest.raises(GalaxyError) as excinfo:
        raise GalaxyError(http_error, "An error occurred while trying to access the Galaxy API.")
    
    assert str(excinfo.value) == "An error occurred while trying to access the Galaxy API. (HTTP Code: 404, Message: Not Found)"
