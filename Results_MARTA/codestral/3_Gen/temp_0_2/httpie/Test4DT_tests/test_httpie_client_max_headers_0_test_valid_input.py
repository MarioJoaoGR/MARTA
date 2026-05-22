
import pytest
from unittest.mock import patch
import http.client

def max_headers(limit):
    orig = http.client._MAXHEADERS
    http.client._MAXHEADERS = limit or float('Inf')
    try:
        yield
    finally:
        http.client._MAXHEADERS = orig

@pytest.fixture(autouse=True)
def reset_max_headers():
    with patch('http.client._MAXHEADERS', new_callable=lambda: 100):
        yield

def test_max_headers():
    assert http.client._MAXHEADERS == 100
