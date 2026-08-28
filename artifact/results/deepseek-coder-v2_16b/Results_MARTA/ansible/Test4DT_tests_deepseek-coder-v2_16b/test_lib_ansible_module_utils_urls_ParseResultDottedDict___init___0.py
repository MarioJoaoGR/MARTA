
import pytest
from ansible.module_utils.urls import ParseResultDottedDict

def test_parseresultdotteddict_initialization():
    result = ParseResultDottedDict(scheme='http', netloc='example.com', path='/path')
    assert result.scheme == 'http'
    assert result.netloc == 'example.com'
    assert result.path == '/path'

def test_parseresultdotteddict_modification():
    result = ParseResultDottedDict(scheme='http', netloc='example.com', path='/path')
    result['netloc'] = 'newdomain.com'
    assert result.netloc == 'newdomain.com'

def test_parseresultdotteddict_access():
    result = ParseResultDottedDict(scheme='http', netloc='example.com', path='/path')
    assert result.scheme == 'http'
    assert result.netloc == 'example.com'
    assert result.path == '/path'

def test_parseresultdotteddict_as_list():
    parse_result = ParseResultDottedDict(scheme='http', netloc='example.com', path='/path', params='', query='query=value', fragment='frag')
    parsed_list = parse_result.as_list()
    assert parsed_list == ['http', 'example.com', '/path', '', 'query=value', 'frag']
