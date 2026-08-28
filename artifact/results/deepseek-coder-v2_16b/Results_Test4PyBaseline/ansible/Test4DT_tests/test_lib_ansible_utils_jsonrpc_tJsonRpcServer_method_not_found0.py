
# Module: ansible.utils.jsonrpc
# Import the function from the module
from ansible.utils.jsonrpc import JsonRpcServer
import json

def test_JsonRpcServer_method_not_found():
    # Create an instance of JsonRpcServer
    server = JsonRpcServer()
    
    # Call method_not_found and check if it returns the expected error response
    response = server.method_not_found()
    assert response["jsonrpc"] == "2.0"
    assert response["id"] is None
    assert response["error"]["code"] == -32601
    assert response["error"]["message"] == "Method not found"
    assert isinstance(response["error"]["data"], dict)

def test_JsonRpcServer_method_not_found_with_data():
    # Create an instance of JsonRpcServer
    server = JsonRpcServer()
    
    # Call method_not_found with data and check if it returns the expected error response with data
    response = server.method_not_found({"additional": "info"})
    assert response["jsonrpc"] == "2.0"
    assert response["id"] is None
    assert response["error"]["code"] == -32601
    assert response["error"]["message"] == "Method not found"
    assert response["error"]["data"] == {"additional": "info"}
