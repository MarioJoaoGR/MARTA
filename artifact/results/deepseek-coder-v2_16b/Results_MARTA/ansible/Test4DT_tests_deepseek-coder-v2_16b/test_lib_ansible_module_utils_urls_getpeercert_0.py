
import pytest
from unittest.mock import patch
import urllib.request
from ansible.module_utils.urls import getpeercert


def test_getpeercert_non_https():
    class MockHTTPResponse:
        fp = None  # Assuming this is enough to simulate a non-HTTPS response

    response = MockHTTPResponse()
    with pytest.raises(AttributeError):
        getpeercert(response)