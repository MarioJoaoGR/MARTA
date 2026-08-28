
import pytest
from ansible.module_utils.urls import url_argument_spec

def test_url_argument_spec():
    arg_spec = url_argument_spec()
    assert 'url' in arg_spec
    assert arg_spec['url'] == {'type': 'str'}

def test_force_argument_spec():
    arg_spec = url_argument_spec()
    assert 'force' in arg_spec
    assert arg_spec['force'] == {'type': 'bool', 'default': False, 'aliases': ['thirsty'], 'deprecated_aliases': [{'name': 'thirsty', 'version': '2.13', 'collection_name': 'ansible.builtin'}]}

def test_http_agent_argument_spec():
    arg_spec = url_argument_spec()
    assert 'http_agent' in arg_spec
    assert arg_spec['http_agent'] == {'type': 'str', 'default': 'ansible-httpget'}

def test_use_proxy_argument_spec():
    arg_spec = url_argument_spec()
    assert 'use_proxy' in arg_spec
    assert arg_spec['use_proxy'] == {'type': 'bool', 'default': True}

def test_validate_certs_argument_spec():
    arg_spec = url_argument_spec()
    assert 'validate_certs' in arg_spec
    assert arg_spec['validate_certs'] == {'type': 'bool', 'default': True}

def test_url_username_argument_spec():
    arg_spec = url_argument_spec()
    assert 'url_username' in arg_spec
    assert arg_spec['url_username'] == {'type': 'str'}

def test_url_password_argument_spec():
    arg_spec = url_argument_spec()
    assert 'url_password' in arg_spec
    assert arg_spec['url_password'] == {'type': 'str', 'no_log': True}

def test_force_basic_auth_argument_spec():
    arg_spec = url_argument_spec()
    assert 'force_basic_auth' in arg_spec
    assert arg_spec['force_basic_auth'] == {'type': 'bool', 'default': False}

def test_client_cert_argument_spec():
    arg_spec = url_argument_spec()
    assert 'client_cert' in arg_spec
    assert arg_spec['client_cert'] == {'type': 'path'}

def test_client_key_argument_spec():
    arg_spec = url_argument_spec()
    assert 'client_key' in arg_spec
    assert arg_spec['client_key'] == {'type': 'path'}

def test_use_gssapi_argument_spec():
    arg_spec = url_argument_spec()
    assert 'use_gssapi' in arg_spec
    assert arg_spec['use_gssapi'] == {'type': 'bool', 'default': False}
