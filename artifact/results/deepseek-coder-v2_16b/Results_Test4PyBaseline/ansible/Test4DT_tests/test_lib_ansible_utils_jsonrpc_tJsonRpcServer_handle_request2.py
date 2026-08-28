
import pytest
from ansible.utils.jsonrpc import JsonRpcServer
import json
import traceback
from unittest.mock import patch

# Fixture to create a JsonRpcServer instance for each test
@pytest.fixture
def server():
    return JsonRpcServer()

# Test handling of basic JSON-RPC request
def test_handle_request_basic(server):
    request = '{"method": "add", "params": [1, 2], "id": 1}'
    response = server.handle_request(request)
    assert isinstance(response, str), f"Expected a JSON string response but got {type(response)}"
    parsed_response = json.loads(response)