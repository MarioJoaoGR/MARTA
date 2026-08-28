
import pytest
from ansible.module_utils.urls import ParseResultDottedDict

def test_parseresultdotteddict_initialization():
    # Test initialization with keyword arguments
    result = ParseResultDottedDict(scheme='http', netloc='example.com', path='/path')
    assert result.scheme == 'http'
    assert result.netloc == 'example.com'
    assert result.path == '/path'
    
    # Test initialization with dictionary
    kwargs = {
        'scheme': 'https',
        'netloc': 'secure.example.com',
        'path': '/secured/path'
    }
    result_dict = ParseResultDottedDict(**kwargs)
    assert result_dict.scheme == 'https'
    assert result_dict.netloc == 'secure.example.com'
    assert result_dict.path == '/secured/path'
    
def test_parseresultdotteddict_as_list():
    # Test as_list method
    parse_result = ParseResultDottedDict(scheme='http', netloc='example.com', path='/path', params='', query='query=value', fragment='frag')
    parsed_list = parse_result.as_list()
    assert parsed_list == ['http', 'example.com', '/path', '', 'query=value', 'frag']
    
def test_parseresultdotteddict_update():
    # Test updating values
    result = ParseResultDottedDict(scheme='http', netloc='example.com', path='/path')
    assert result.netloc == 'example.com'
    result['netloc'] = 'newdomain.com'
    assert result.netloc == 'newdomain.com'
