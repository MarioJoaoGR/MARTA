
import pytest
from ansible.utils.jsonrpc import JsonRpcServer

def test_valid_input():
    server = JsonRpcServer()
    response = server.invalid_params()
    assert response == {'jsonrpc': '2.0', 'error': {'code': -32602, 'message': 'Invalid params'}}

def test_edge_case_none():
    server = JsonRpcServer()
    with pytest.raises(TypeError):
        server.invalid_params(None)  # This should raise a TypeError because the method does not accept None as an argument

def test_invalid_input():
    server = JsonRpcServer()
    with pytest.raises(ValueError):
        server.invalid_params({"reason": "Type mismatch"})  # This should raise a ValueError because the error code is fixed and cannot be overridden by additional data
