
import pytest
from unittest.mock import patch
from httpie.client import HTTPHeadersDict

# Define SKIPPABLE_HEADERS and SKIP_HEADER as constants within the function
def finalize_headers(headers: HTTPHeadersDict) -> HTTPHeadersDict:
    SKIPPABLE_HEADERS = {'Content-Type', 'Set-Cookie'}
    SKIP_HEADER = None
    final_headers = HTTPHeadersDict()
    for name, value in headers.items():
        if value is not None:
            # “leading or trailing LWS MAY be removed without changing the semantics of the field value”
            # <https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html>
            # Also, requests raises `InvalidHeader` for leading spaces.
            value = value.strip()
            if isinstance(value, str):
                # See <https://github.com/httpie/cli/issues/212>
                value = value.encode()
        elif name.lower() in SKIPPABLE_HEADERS:
            # Some headers get overwritten by urllib3 when set to `None` and should be replaced with the `SKIP_HEADER` constant.
            value = SKIP_HEADER
        final_headers.add(name, value)
    return final_headers

# Test case for edge case where no headers are provided
def test_edge_case_none():
    headers = HTTPHeadersDict()
    with patch('httpie.client.HTTPHeadersDict') as mock_headers:
        # Mock the behavior of HTTPHeadersDict to return a new instance
        mock_headers.return_value = HTTPHeadersDict()
        
        result = finalize_headers(headers)
        assert isinstance(result, HTTPHeadersDict), "The result should be an instance of HTTPHeadersDict"
