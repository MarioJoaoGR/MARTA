
import pytest
from urllib.parse import urlparse, urlunparse
from unittest.mock import patch

def ensure_path_as_is(orig_url: str, prepped_url: str) -> str:
    """
    Handle `--path-as-is` by replacing the path component of the prepared URL with the path component from the original URL. Other parts stay untouched because other (welcome) processing on the URL might have taken place.

    The function is designed to ensure that the path component of a URL, which has been processed in some way, reverts back to its original form as specified in the `orig_url`. This is particularly useful when subsequent operations or transformations should respect the originally intended path specification, overriding any modifications made during the preparation process.

    Parameters:
        orig_url (str): The original URL from which to take the path component. This should be a valid URL string.
        prepped_url (str): The prepared URL whose path component needs to be replaced with that of `orig_url`. This should also be a valid URL string.

    Returns:
        str: A new URL where the path component is taken from `orig_url` and other parts are preserved as in `prepped_url`.

    Examples:
        >>> ensure_path_as_is('http://foo/../', 'http://foo/?foo=bar')
        'http://foo/../?foo=bar'

    Notes:
        - Both `orig_url` and `prepped_url` must be valid URL strings.
        - The function uses the `urlparse` from Python's `urllib.parse` to parse both URLs, then constructs a new URL with the path component replaced as specified.
    """
    parsed_orig, parsed_prepped = urlparse(orig_url), urlparse(prepped_url)
    final_dict = {
        # noinspection PyProtectedMember
        **parsed_prepped._asdict(),
        'path': parsed_orig.path,
    }
    return urlunparse(tuple(final_dict.values()))

@pytest.fixture(autouse=True)
def mock_urlparse():
    with patch('urllib.parse.urlparse') as mock_urlparse:
        yield mock_urlparse

@pytest.mark.parametrize("orig_url, prepped_url, expected", [
    ('http://foo/../', 'http://foo/?foo=bar', 'http://foo/../?foo=bar'),
    ('https://example.com/path/', 'https://example.com/?query=test', 'https://example.com/path/?query=test'),
    ('ftp://example.org/docs/', 'ftp://example.org/other-docs/?param=value', 'ftp://example.org/docs/?param=value')
])
def test_valid_input(orig_url, prepped_url, expected):
    with patch('urllib.parse.urlparse', return_value=urlparse(prepped_url)):
        assert ensure_path_as_is(orig_url, prepped_url) == expected
