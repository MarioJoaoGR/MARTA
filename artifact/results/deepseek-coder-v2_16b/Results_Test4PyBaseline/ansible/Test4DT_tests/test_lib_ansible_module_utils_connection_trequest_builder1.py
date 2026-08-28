
# Module: ansible.module_utils.connection
import pytest
import uuid
from ansible.module_utils.connection import request_builder

def test_request_builder_uuid():
    method_name = 'example_method'
    request = request_builder(method_name)
    assert request['jsonrpc'] == '2.0'  # Line 106: Ensure jsonrpc is set to '2.0'
    assert request['method'] == method_name  # Line 106: Ensure method is set correctly
    assert isinstance(request['id'], str)  # Line 105: Ensure id is a UUID string
    assert len(request['id']) == 36  # UUID length is 36 characters
    assert request['params'] == ((), {})  # Line 107: Ensure params are correctly formatted

def test_request_builder_uuid_length():
    method_name = 'example_method'
    request = request_builder(method_name)
    assert len(request['id']) == 36  # UUID length is always 36 characters

def test_request_builder_params_format():
    method_name = 'example_method'
    request = request_builder(method_name)
    assert request['params'] == ((), {})  # Ensure params are correctly formatted as an empty tuple and dictionary

def test_request_builder_returns_dict():
    method_name = 'example_method'
    request = request_builder(method_name)
    assert isinstance(request, dict)  # Line 109: Ensure the function returns a dictionary
