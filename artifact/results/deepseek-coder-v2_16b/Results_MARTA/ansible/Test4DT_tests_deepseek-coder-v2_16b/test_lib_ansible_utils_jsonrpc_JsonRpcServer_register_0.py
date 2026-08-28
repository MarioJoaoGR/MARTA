
import pytest
from ansible.utils.jsonrpc import JsonRpcServer

# Test for valid input scenario
def test_valid_input():
    server = JsonRpcServer()
    obj1 = SomeObject()
    obj2 = AnotherObject()
    
    # Registering objects with the server
    server.register(obj1)
    server.register(obj2)
    
    assert len(server._objects) == 2, "Expected two objects to be registered but found something else."
    assert obj1 in server._objects, "Object obj1 is not registered in the server."
    assert obj2 in server._objects, "Object obj2 is not registered in the server."

# Test for handling None input scenario
def test_none_input():
    server = JsonRpcServer()
    with pytest.raises(TypeError):
        server.register(None)

# Test for handling duplicate object registration scenario
def test_duplicate_input():
    server = JsonRpcServer()
    obj1 = SomeObject()
    server.register(obj1)
    
    with pytest.raises(ValueError):
        server.register(obj1)
