
import json
import pytest
from ansible.utils.jsonrpc import JsonRpcServer

# Fixture to create a valid JSON-RPC request
@pytest.fixture
def valid_request():
    return '{"method": "add", "params": [1, 2], "id": 1}'

# Fixture to create an invalid JSON-RPC request
@pytest.fixture
def invalid_request():
    return '{"method": "rpc.reservedMethod", "params": [1, 2], "id": 1}'

# Fixture to create a request with an unknown method
@pytest.fixture
def unknown_method_request():
    return '{"method": "unknownMethod", "params": [1, 2], "id": 1}'

# Test for handling a valid JSON-RPC request
def test_valid_input(valid_request):
    server = JsonRpcServer()
    obj1 = SomeObject()
    server.register(obj1)
    response = server.handle_request(valid_request)
    parsed_response = json.loads(response)
    assert parsed_response['jsonrpc'] == '2.0'
    assert parsed_response['id'] == 1
    assert isinstance(parsed_response['result'], int)

# Test for handling a JSON-RPC request with an invalid method
def test_invalid_request(invalid_request):
    server = JsonRpcServer()
    response = server.handle_request(invalid_request)
    parsed_response = json.loads(response)
    assert parsed_response['jsonrpc'] == '2.0'
    assert parsed_response['id'] == 1
    assert parsed_response['error']['code'] == -32600

# Test for handling a JSON-RPC request with an unknown method and error propagation
def test_error_handling(unknown_method_request):
    server = JsonRpcServer()
    response = server.handle_request(unknown_method_request)
    parsed_response = json.loads(response)
    assert parsed_response['jsonrpc'] == '2.0'
    assert parsed_response['id'] == 1
    assert parsed_response['error']['code'] == -32601
