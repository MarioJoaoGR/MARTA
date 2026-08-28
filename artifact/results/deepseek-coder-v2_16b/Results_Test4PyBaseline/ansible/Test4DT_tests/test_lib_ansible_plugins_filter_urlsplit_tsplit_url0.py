# Module: ansible.plugins.filter.urlsplit
import pytest
from ansible.plugins.filter import urlsplit as split_url_module
from ansible.errors import AnsibleFilterError

# Import the function using its module name
split_url = split_url_module.split_url

def test_split_url_basic():
    result = split_url('http://example.com/path?query=value#fragment')
    assert isinstance(result, dict), "Expected a dictionary but got {}".format(type(result))
    assert set(result.keys()) == {'scheme', 'netloc', 'path', 'params', 'query', 'fragment'}, "Unexpected keys in result: {}".format(result.keys())
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.com'
    assert result['path'] == '/path'
    assert result['params'] == ''
    assert result['query'] == 'query=value'
    assert result['fragment'] == 'fragment'

def test_split_url_specific_component():
    result = split_url('http://example.com/path?query=value#fragment', 'path')
    assert isinstance(result, str), "Expected a string but got {}".format(type(result))
    assert result == '/path'

def test_split_url_default_alias():
    result = split_url('http://example.com/path?query=value#fragment', query='path')
    assert isinstance(result, str), "Expected a string but got {}".format(type(result))
    assert result == '/path'

def test_split_url_unknown_component():
    with pytest.raises(AnsibleFilterError) as e:
        split_url('http://example.com/path?query=value#fragment', 'unknown')
    assert str(e.value) == "ansible.plugins.filter.urlsplit: unknown URL component: unknown"
