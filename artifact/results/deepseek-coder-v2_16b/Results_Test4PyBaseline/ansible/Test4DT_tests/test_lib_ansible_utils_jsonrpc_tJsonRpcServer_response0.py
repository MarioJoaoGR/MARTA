
# Module: ansible.utils.jsonrpc
import pytest
from ansible.utils.jsonrpc import JsonRpcServer, to_text, cPickle

# Fixture to create an instance of JsonRpcServer for testing
@pytest.fixture
def server():
    return JsonRpcServer()

# Test cases for the response method
def test_default_response(server):
    """Test default response without any result."""
    assert server.response() == {'jsonrpc': '2.0', 'id': None, 'result': None, 'result_type': 'pickle'}

def test_response_with_dict_result(server):
    """Test response with a dictionary as result."""
    result = {'key': 'value'}
    assert server.response(result) == {'jsonrpc': '2.0', 'id': None, 'result': result, 'result_type': 'pickle'}

def test_response_with_list_result(server):
    """Test response with a list as result."""
    result = [1, 2, 3]
    assert server.response(result) == {'jsonrpc': '2.0', 'id': None, 'result': to_text(cPickle.dumps(result, protocol=0)), 'result_type': 'pickle'}

def test_response_with_binary_result(server):
    """Test response with a binary type result."""
    binary_result = b'binary data'
    assert server.response(binary_result) == {'jsonrpc': '2.0', 'id': None, 'result': to_text(binary_result), 'result_type': 'pickle'}

def test_response_with_string_result(server):
    """Test response with a string result."""
    string_result = 'plain text'
    assert server.response(string_result) == {'jsonrpc': '2.0', 'id': None, 'result': string_result, 'result_type': 'pickle'}
