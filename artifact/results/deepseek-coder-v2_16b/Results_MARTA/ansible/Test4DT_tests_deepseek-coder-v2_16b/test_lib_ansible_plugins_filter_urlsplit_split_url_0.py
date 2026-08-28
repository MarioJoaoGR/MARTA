
import pytest
from ansible.plugins.filter import urlsplit
from urllib.parse import urlparse

# Mocking the AnsibleFilterError for testing purposes
class AnsibleFilterError(Exception):
    pass

def split_url(value, query='', alias='urlsplit'):
    results = helpers.object_to_dict(urlsplit(value), exclude=['count', 'index', 'geturl', 'encode'])

    if query:
        if query not in results:
            raise AnsibleFilterError(alias + ': unknown URL component: %s' % query)
        return results[query]
    else:
        return results

# Test function for valid input happy path
def test_valid_input_happy_path():
    result = split_url('http://example.com/path?query=value#fragment')
    expected = {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/path',
        'params': '',
        'query': 'query=value',
        'fragment': 'fragment'
    }
    assert result == expected

# Test function for querying a specific component of the URL
def test_specific_component_query():
    result = split_url('http://example.com/path?query=value#fragment', 'netloc')
    assert result == 'example.com'

# Test function for handling an unknown URL component query
def test_invalid_component_query():
    with pytest.raises(AnsibleFilterError):
        split_url('http://example.com/path?query=value#fragment', 'unknown_component')
