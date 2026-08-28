# Module: ansible.module_utils.connection
import pytest
import uuid
from ansible.module_utils.connection import request_builder

def test_request_builder_simple():
    method_name = 'example_method'
    request = request_builder(method_name)
    assert request['jsonrpc'] == '2.0'
    assert request['method'] == method_name
    assert isinstance(request['id'], str)
    assert len(request['id']) == 36  # UUID length is 36 characters
    assert request['params'] == ((), {})

def test_request_builder_complex():
    method_name = 'complex_method'
    positional_args = ['positional1', 'positional2']
    keyword_args = {'key1': 'value1', 'key2': 'value2'}
    request = request_builder(method_name, *positional_args, **keyword_args)
    assert request['jsonrpc'] == '2.0'
    assert request['method'] == method_name
    assert isinstance(request['id'], str)
    assert len(request['id']) == 36
    assert request['params'] == (positional_args, keyword_args)

def test_request_builder_no_parameters():
    method_name = 'another_method'
    request = request_builder(method_name)
    assert request['jsonrpc'] == '2.0'
    assert request['method'] == method_name
    assert isinstance(request['id'], str)
    assert len(request['id']) == 36
    assert request['params'] == ((), {})

def test_request_builder_positional_only():
    method_name = 'yet_another_method'
    positional_args = ['positional3', 'positional4']
    request = request_builder(method_name, *positional_args)
    assert request['jsonrpc'] == '2.0'
    assert request['method'] == method_name
    assert isinstance(request['id'], str)
    assert len(request['id']) == 36
    assert request['params'] == (positional_args, {})

def test_request_builder_keyword_only():
    method_name = 'final_method'
    keyword_args = {'key1': 'value3', 'key2': 'value4'}
    request = request_builder(method_name, **keyword_args)
    assert request['jsonrpc'] == '2.0'
    assert request['method'] == method_name
    assert isinstance(request['id'], str)
    assert len(request['id']) == 36
    assert request['params'] == ((), keyword_args)
