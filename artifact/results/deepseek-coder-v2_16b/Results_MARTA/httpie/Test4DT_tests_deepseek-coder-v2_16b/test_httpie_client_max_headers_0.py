
import pytest
from unittest.mock import patch
import http.client

def max_headers(limit):
    orig = http.client._MAXHEADERS
    if limit is None or limit <= 0:
        limit = float('Inf')
    http.client._MAXHEADERS = limit
    try:
        yield
    finally:
        http.client._MAXHEADERS = orig



def test_invalid_input_negative_number():
    with patch('http.client._MAXHEADERS', new=32) as original_max_headers:
        with pytest.raises(AttributeError):
            with max_headers(-5):
                pass