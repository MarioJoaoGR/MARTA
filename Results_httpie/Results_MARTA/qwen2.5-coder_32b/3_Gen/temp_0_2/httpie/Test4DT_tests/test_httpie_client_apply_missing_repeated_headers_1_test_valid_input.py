
import pytest
from httpie.client import HTTPHeadersDict, requests

def apply_missing_repeated_headers(
    original_headers: HTTPHeadersDict,
    prepared_request: requests.PreparedRequest
) -> None:
    """Update the given `prepared_request`'s headers with the original ones."""
    new_headers = HTTPHeadersDict(prepared_request.headers)
    for prepared_name, prepared_value in prepared_request.headers.items():
        if prepared_name not in original_headers:
            continue

        original_keys, original_values = zip(*filter(
            lambda item: item[0].casefold() == prepared_name.casefold(),
            original_headers.items()
        ))

        if prepared_value not in original_values:
            # If the current value is not among the initial values
            # set for this field, then it means that this field got
            # overridden on the way, and we should preserve it.
            continue

        new_headers.popone(prepared_name)
        new_headers.update(zip(original_keys, original_values))

    prepared_request.headers = new_headers

# Test case for valid input
def test_valid_input():
    from unittest.mock import patch
    from httpie.client import requests

    # Mocking the necessary parts of the requests library
    with patch('httpie.client.requests') as mock_requests:
        original_headers = HTTPHeadersDict({'Content-Type': 'application/json'})
        prepared_request = mock_requests.PreparedRequest()
        prepared_request.headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer token'}

        apply_missing_repeated_headers(original_headers, prepared_request)

        assert prepared_request.headers == {'Content-Type': 'application/json', 'Authorization': 'Bearer token'}
