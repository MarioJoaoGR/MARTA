
import sys
from unittest.mock import patch
import pytest
import requests

def dump_request(kwargs: dict):
    """
    Sends a request using the `requests` library based on the provided keyword arguments.

    Parameters:
        kwargs (dict): A dictionary containing the parameters needed to construct and send an HTTP request. This includes methods like 'method', 'url', 'params', 'data', 'headers', etc., which are used by the `requests.request` function.

    Returns:
        None

    Example:
        >>> dump_request({'method': 'GET', 'url': 'https://api.example.com/data'})
        >>> requests.request('GET', 'https://api.example.com/data')

    This function writes the equivalent `requests.request` call to standard error, allowing for easy inspection and debugging of the request parameters before execution. It is useful for developers who need to ensure that their HTTP request configuration is correct before proceeding with actual requests in a production environment.
    """
    sys.stderr.write(f'\n>>> requests.request(**{repr_dict(kwargs)})\n\n')

def repr_dict(d: dict) -> str:
    return ', '.join([f'{k}={v!r}' for k, v in d.items()])

@pytest.mark.parametrize("invalid_input", [
    {'method': 'GET', 'url': 'https://api.example.com/data'},
    {'method': 'POST', 'url': 'https://api.example.com/data', 'data': None},
    {'method': 'PUT', 'url': 'https://api.example.com/data', 'headers': {}},
])
def test_invalid_input(invalid_input):
    with patch('sys.stderr') as mock_stderr:
        dump_request(invalid_input)
        assert mock_stderr.write.called
