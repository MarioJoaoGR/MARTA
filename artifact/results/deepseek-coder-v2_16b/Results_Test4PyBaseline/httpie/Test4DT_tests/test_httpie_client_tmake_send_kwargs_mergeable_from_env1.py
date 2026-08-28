
import argparse
import pytest
from httpie.client import make_send_kwargs_mergeable_from_env

# Test default values
def test_make_send_kwargs_mergeable_from_env_default():
    args = argparse.Namespace(cert=None, cert_key=None, proxy=[argparse.Namespace(key='http', value='http://example.com')], verify='yes')
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert isinstance(kwargs, dict), "Expected a dictionary"
    assert 'proxies' in kwargs, "Expected 'proxies' key in the dictionary"
    assert kwargs['proxies'] == {'http': 'http://example.com'}, "Unexpected proxy value"
    assert 'stream' in kwargs, "Expected 'stream' key in the dictionary"
    assert kwargs['stream'] is True, "Unexpected stream mode"
    assert kwargs['verify'] is True, "Unexpected verify value"
    assert kwargs['cert'] is None, "Unexpected cert value"

# Test case for when only cert is provided
def test_make_send_kwargs_mergeable_from_env_cert_only():
    args = argparse.Namespace(cert='path/to/cert', cert_key=None, proxy=[argparse.Namespace(key='http', value='http://example.com')], verify='yes')
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert isinstance(kwargs, dict), "Expected a dictionary"
    assert 'proxies' in kwargs, "Expected 'proxies' key in the dictionary"
    assert kwargs['proxies'] == {'http': 'http://example.com'}, "Unexpected proxy value"
    assert 'stream' in kwargs, "Expected 'stream' key in the dictionary"
    assert kwargs['stream'] is True, "Unexpected stream mode"
    assert kwargs['verify'] is True, "Unexpected verify value"
    assert kwargs['cert'] == 'path/to/cert', "Unexpected cert value"

# Test case for when only cert_key is provided
def test_make_send_kwargs_mergeable_from_env_cert_key_only():
    args = argparse.Namespace(cert=None, cert_key='path/to/cert_key', proxy=[argparse.Namespace(key='http', value='http://example.com')], verify='yes')
    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert isinstance(kwargs, dict), "Expected a dictionary"
    assert 'proxies' in kwargs, "Expected 'proxies' key in the dictionary"
    assert kwargs['proxies'] == {'http': 'http://example.com'}, "Unexpected proxy value"
    assert 'stream' in kwargs, "Expected 'stream' key in the dictionary"
    assert kwargs['stream'] is True, "Unexpected stream mode"
    assert kwargs['verify'] is True, "Unexpected verify value"