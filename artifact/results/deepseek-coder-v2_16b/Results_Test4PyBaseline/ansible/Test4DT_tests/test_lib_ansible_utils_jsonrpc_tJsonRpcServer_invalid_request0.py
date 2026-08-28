
import pytest
from ansible.utils.jsonrpc import JsonRpcServer

# Test cases for the invalid_request method in the JsonRpcServer class
def test_invalid_request_basic():
    server = JsonRpcServer()
    response = server.invalid_request()
    assert response == {'jsonrpc': '2.0', 'id': None, 'error': {'code': -32600, 'message': 'Invalid request'}}

def test_invalid_request_with_data():
    server = JsonRpcServer()
    response = server.invalid_request({"detail": "Missing 'method' field"})
    assert response == {'jsonrpc': '2.0', 'id': None, 'error': {'code': -32600, 'message': 'Invalid request', 'data': {'detail': "Missing 'method' field"}}}
