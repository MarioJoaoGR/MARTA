
import json
import pytest
from ansible.utils.jsonrpc import JsonRpcServer

# Fixture to create a JsonRpcServer instance for each test
@pytest.fixture(scope="module")
def server():
    return JsonRpcServer()

# Test for handling a valid JSON-RPC request

# Test for handling a JSON-RPC request with an invalid method

# Test for handling a JSON-RPC request with an unknown method
def test_unknown_method(server):
    unknown_method_request = '{"method": "unknownMethod", "params": [1, 2], "id": 1}'
    response = server.handle_request(unknown_method_request)
    error = json.loads(response)
    assert error['error']['code'] == -32601
    assert 'Method not found' in error['error']['message']