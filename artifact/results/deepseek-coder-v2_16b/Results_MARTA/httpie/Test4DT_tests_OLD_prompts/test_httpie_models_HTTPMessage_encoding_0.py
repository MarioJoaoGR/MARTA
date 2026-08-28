
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPRequest
import requests
from urllib.parse import urlsplit

# Test 1: Initialize HTTPMessage with valid original data

# Test 2: Initialize HttpRequest with method, path, headers, and body

# Test 3: Initialize HttpRequest with default version and empty headers

# Test 4: Initialize HttpRequest with empty headers and no body

# Test 5: Initialize HttpRequest with invalid method should raise an exception
def test_httprequest_invalid_method():
    with pytest.raises(Exception):
        HttpRequest(method='INVALID', path='/error', headers={'Host': 'example.com'})