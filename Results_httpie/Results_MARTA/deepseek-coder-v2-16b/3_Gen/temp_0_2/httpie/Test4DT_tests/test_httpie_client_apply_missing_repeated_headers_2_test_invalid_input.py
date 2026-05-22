
import requests
from httpie.client import HTTPHeadersDict
from unittest.mock import patch, MagicMock

def apply_missing_repeated_headers(
    original_headers: HTTPHeadersDict,
    prepared_request: requests.PreparedRequest
) -> None:
    """Update the given `prepared_request`'s headers with the original ones. This allows the requests to be prepared as usual, and then later merged with headers that are specified multiple times."""

    new_headers = HTTPHeadersDict(prepared_request.headers)
    for prepared_name, prepared_value in prepared_request.headers.items():
        if prepared_name not in original_headers:
            continue

        original_keys, original_values = zip(*filter(
            lambda item: item[0].casefold() == prepared_name.casefold(),
            original_headers.items()
        ))

        if prepared_value not in original_values:
            # If the current value is not among the initial values set for this field, then it means that this field got overridden on the way, and we should preserve it.
            continue

        new_headers.popone(prepared_name)
        new_headers.update(zip(original_keys, original_values))

    prepared_request.headers = new_headers

# Example test case using unittest.mock.patch to mock requests.PreparedRequest
def test_invalid_input():
    with patch('httpie.client.HTTPHeadersDict') as MockHTTPHeadersDict:
        with patch('requests.PreparedRequest', autospec=True) as MockPreparedRequest:
            # Arrange
            original_headers = MockHTTPHeadersDict.return_value
            prepared_request = MockPreparedRequest.return_value
            prepared_request.headers = {'Content-Type': 'application/json'}
            original_headers.items.return_value = [('Content-Type', 'application/json')]

            # Act
            apply_missing_repeated_headers(original_headers, prepared_request)

            # Assert
            assert prepared_request.headers == {'Content-Type': 'application/json'}
