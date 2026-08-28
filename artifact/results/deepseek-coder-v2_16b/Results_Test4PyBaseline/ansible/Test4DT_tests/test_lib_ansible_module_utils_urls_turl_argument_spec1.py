
import pytest
from ansible.module_utils.urls import url_argument_spec

def test_url_argument_spec():
    arg_spec = url_argument_spec()
    
    # Check the type of each argument in the returned dictionary
    assert isinstance(arg_spec['url'], dict)
    assert isinstance(arg_spec['force'], dict)
    assert isinstance(arg_spec['http_agent'], dict)
    assert isinstance(arg_spec['use_proxy'], dict)
    assert isinstance(arg_spec['validate_certs'], dict)
    assert isinstance(arg_spec['url_username'], dict)
    assert isinstance(arg_spec['url_password'], dict)
    assert isinstance(arg_spec['force_basic_auth'], dict)
    assert isinstance(arg_spec['client_cert'], dict)
    assert isinstance(arg_spec['client_key'], dict)
    assert isinstance(arg_spec['use_gssapi'], dict)
    
    # Check the default values and types of some arguments
    assert arg_spec['force']['default'] == False
    assert arg_spec['http_agent']['default'] == 'ansible-httpget'
    assert arg_spec['use_proxy']['default'] == True
    assert arg_spec['validate_certs']['default'] == True
    assert arg_spec['force_basic_auth']['default'] == False
    assert arg_spec['use_gssapi']['default'] == False
    
    # Check the aliases and deprecated information
    assert 'aliases' in arg_spec['force']
    assert arg_spec['force']['aliases'] == ['thirsty']
    assert 'deprecated_aliases' in arg_spec['force']
    assert len(arg_spec['force']['deprecated_aliases']) == 1
    deprecated_alias = arg_spec['force']['deprecated_aliases'][0]
    assert deprecated_alias['name'] == 'thirsty'
    assert deprecated_alias['version'] == '2.13'
    assert deprecated_alias['collection_name'] == 'ansible.builtin'
    
    # Check the types of some arguments that should be dicts
    assert isinstance(arg_spec['url'], dict)
    assert isinstance(arg_spec['force'], dict)
    assert isinstance(arg_spec['http_agent'], dict)
    assert isinstance(arg_spec['use_proxy'], dict)
    assert isinstance(arg_spec['validate_certs'], dict)
    assert isinstance(arg_spec['url_username'], dict)
    assert isinstance(arg_spec['url_password'], dict)
    assert isinstance(arg_spec['force_basic_auth'], dict)
    assert isinstance(arg_spec['client_cert'], dict)
    assert isinstance(arg_spec['client_key'], dict)
    assert isinstance(arg_spec['use_gssapi'], dict)
    
    # Check the default values and types of some arguments
    assert arg_spec['force']['default'] == False
    assert arg_spec['http_agent']['default'] == 'ansible-httpget'
    assert arg_spec['use_proxy']['default'] == True
    assert arg_spec['validate_certs']['default'] == True
    assert arg_spec['force_basic_auth']['default'] == False
    assert arg_spec['use_gssapi']['default'] == False
    
    # Check the aliases and deprecated information
    assert 'aliases' in arg_spec['force']
    assert arg_spec['force']['aliases'] == ['thirsty']
    assert 'deprecated_aliases' in arg_spec['force']
    assert len(arg_spec['force']['deprecated_aliases']) == 1
    deprecated_alias = arg_spec['force']['deprecated_aliases'][0]
    assert deprecated_alias['name'] == 'thirsty'
    assert deprecated_alias['version'] == '2.13'
    assert deprecated_alias['collection_name'] == 'ansible.builtin'
