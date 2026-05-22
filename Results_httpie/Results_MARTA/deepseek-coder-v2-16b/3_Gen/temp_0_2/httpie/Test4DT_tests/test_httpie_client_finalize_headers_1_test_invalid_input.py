
import pytest
from unittest.mock import patch
from httpie.client import HTTPHeadersDict, finalize_headers

def test_invalid_input():
    with patch('httpie.client.HTTPHeadersDict', spec=HTTPHeadersDict):
        headers = HTTPHeadersDict({'Invalid-Header': 'value'})
        finalized_headers = finalize_headers(headers)
        assert len(finalized_headers) == 0, "Expected no headers to be present after invalid input"
