
import pytest
from ansible.module_utils.urls import ParseResultDottedDict



def test_as_list_method():
    parse_result = ParseResultDottedDict(scheme='http', netloc='example.com', path='/path', params='', query='query=value', fragment='frag')
    parsed_list = parse_result.as_list()
    assert parsed_list == ['http', 'example.com', '/path', '', 'query=value', 'frag']