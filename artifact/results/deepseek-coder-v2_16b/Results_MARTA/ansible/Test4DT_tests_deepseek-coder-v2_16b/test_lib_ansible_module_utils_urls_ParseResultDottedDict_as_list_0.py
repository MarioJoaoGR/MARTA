
import pytest
from ansible.module_utils.urls import ParseResultDottedDict

def test_valid_initialization():
    result = ParseResultDottedDict(scheme='http', netloc='example.com', path='/path')
    assert result.scheme == 'http'
    assert result.netloc == 'example.com'
    assert result.path == '/path'


def test_as_list_method():
    parse_result = ParseResultDottedDict(scheme='http', netloc='example.com', path='/path', params='', query='query=value', fragment='frag')
    parsed_list = parse_result.as_list()
    assert parsed_list == ['http', 'example.com', '/path', '', 'query=value', 'frag']

def test_update_values():
    result = ParseResultDottedDict(scheme='http', netloc='example.com', path='/path')
    result['netloc'] = 'newdomain.com'
    assert result.netloc == 'newdomain.com'