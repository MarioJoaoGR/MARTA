
import pytest
from ansible.module_utils.urls import url_argument_spec

def test_url_argument_spec_with_empty_dict():
    empty_dict = {}
    edge_case_arg_spec = url_argument_spec(**empty_dict)
    
    assert edge_case_arg_spec['force'] == {'type': 'bool', 'default': False, 'aliases': ['thirsty'], 'deprecated_aliases': [{'name': 'thirsty', 'version': '2.13', 'collection_name': 'ansible.builtin'}]}
    assert edge_case_arg_spec['http_agent'] == {'type': 'str', 'default': 'ansible-httpget'}
    assert edge_case_arg_spec['use_proxy'] == {'type': 'bool', 'default': True}
    assert edge_case_arg_spec['validate_certs'] == {'type': 'bool', 'default': True}
    assert isinstance(edge_case_arg_spec['url_username'], dict)
    assert isinstance(edge_case_arg_spec['url_password'], dict)
    assert edge_case_arg_spec['force_basic_auth'] == {'type': 'bool', 'default': False}
    assert isinstance(edge_case_arg_spec['client_cert'], dict)
    assert isinstance(edge_case_arg_spec['client_key'], dict)
    assert edge_case_arg_spec['use_gssapi'] == {'type': 'bool', 'default': False}

def test_url_argument_spec_with_none_values():
    none_values = [None, None]
    
    with pytest.raises(TypeError):
        url_argument_spec(**none_values)
