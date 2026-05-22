
from urllib.parse import urlsplit
import pytest

def url_as_host(url: str) -> str:
    """
    Extracts the host part from a given URL string.

    This function takes a URL as input and returns the host component of that URL. It uses the `urlsplit` method from the Python standard library to parse the URL, then extracts the netloc (network location) which includes the host and optionally the port number, and finally selects the last part after splitting by '@'.

    Parameters:
        url (str): The input URL string that needs to be parsed. This should be a valid URL with scheme included (e.g., 'http://example.com').

        Returns:
            str: The host part of the provided URL, excluding any username or password if present in the netloc.

    Examples:
        >>> url_as_host('http://example.com')
        'example.com'
        
        >>> url_as_host('https://user:pass@subdomain.example.co.uk/path?query=1#fragment')
        'subdomain.example.co.uk'

    Note:
        - The function assumes that the input URL is well-formed and includes a scheme (e.g., http, https).
        - If the URL contains authentication information (username or password), it will be included in the netloc but not returned by this function.
    """
    parsed_url = urlsplit(url)
    if not parsed_url.scheme:
        raise ValueError("Invalid URL: Missing scheme")
    return parsed_url.netloc.split('@')[-1]

def test_valid_input():
    with pytest.raises(ValueError):
        url_as_host('invalid-url')
