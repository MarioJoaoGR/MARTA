
import pytest
from httpie.models import HTTPResponse
import requests

def test_httpresponse_initialization():
    response = requests.Response()
    http_response = HTTPResponse(response)
    assert isinstance(http_response, HTTPResponse), "Initialization should create an instance of HTTPResponse"
