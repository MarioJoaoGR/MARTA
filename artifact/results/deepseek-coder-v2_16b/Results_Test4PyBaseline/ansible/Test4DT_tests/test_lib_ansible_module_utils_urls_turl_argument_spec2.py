
import pytest
from ansible.module_utils.urls import url_argument_spec

def test_url_argument_spec():
    arg_spec = url_argument_spec()
    
    # Check if the returned value is a dictionary
    assert isinstance(arg_spec, dict)
    
    # Check the expected keys and their types in the dictionary
    assert 'url' in arg_spec
    assert isinstance(arg_spec['url'], dict)
    
    assert 'force' in arg_spec
    assert isinstance(arg_spec['force'], dict)
    assert arg_spec['force']['default'] == False
    
    assert 'http_agent' in arg_spec
    assert isinstance(arg_spec['http_agent'], dict)
    assert arg_spec['http_agent']['default'] == 'ansible-httpget'
    
    assert 'use_proxy' in arg_spec
    assert isinstance(arg_spec['use_proxy'], dict)
    assert arg_spec['use_proxy']['default'] == True
    
    assert 'validate_certs' in arg_spec
    assert isinstance(arg_spec['validate_certs'], dict)
    assert arg_spec['validate_certs']['default'] == True
    
    assert 'url_username' in arg_spec
    assert isinstance(arg_spec['url_username'], dict)
    
    assert 'url_password' in arg_spec
    assert isinstance(arg_spec['url_password'], dict)
    assert arg_spec['url_password']['no_log'] == True
    
    assert 'force_basic_auth' in arg_spec
    assert isinstance(arg_spec['force_basic_auth'], dict)
    assert arg_spec['force_basic_auth']['default'] == False
    
    assert 'client_cert' in arg_spec
    assert isinstance(arg_spec['client_cert'], dict)
    
    assert 'client_key' in arg_spec
    assert isinstance(arg_spec['client_key'], dict)
    
    assert 'use_gssapi' in arg_spec
    assert isinstance(arg_spec['use_gssapi'], dict)
    assert arg_spec['use_gssapi']['default'] == False
