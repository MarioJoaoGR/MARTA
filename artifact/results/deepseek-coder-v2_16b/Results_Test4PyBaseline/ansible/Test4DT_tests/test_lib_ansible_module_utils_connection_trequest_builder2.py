
import pytest
import uuid
from ansible.module_utils.connection import request_builder

def test_request_builder_uuid_generation():
    method_name = 'example_method'
    request = request_builder(method_name)
    
    # Check if UUID is generated and included in the request
    assert isinstance(request['id'], str)
    assert len(request['id']) == 36  # UUID length is 36 characters

def test_request_builder_params_structure():
    method_name = 'example_method'
    positional_args = ['positional1', 'positional2']
    keyword_args = {'key1': 'value1', 'key2': 'value2'}
    request = request_builder(method_name, *positional_args, **keyword_args)
    
    # Check if params is a tuple containing positional and keyword arguments
    assert isinstance(request['params'], tuple)
    assert request['params'] == (tuple(positional_args), keyword_args)

def test_request_builder_no_params():
    method_name = 'example_method'
    request = request_builder(method_name)
    
    # Check if params is an empty tuple when no additional arguments are provided
    assert request['params'] == ((), {})

def test_request_builder_empty_args():
    method_name = 'example_method'
    request = request_builder(method_name, *[])
    
    # Check if params is an empty tuple when no positional arguments are provided
    assert request['params'] == ((), {})

def test_request_builder_empty_kwargs():
    method_name = 'example_method'
    request = request_builder(method_name, **{})
    
    # Check if params is an empty tuple when no keyword arguments are provided
    assert request['params'] == ((), {})
