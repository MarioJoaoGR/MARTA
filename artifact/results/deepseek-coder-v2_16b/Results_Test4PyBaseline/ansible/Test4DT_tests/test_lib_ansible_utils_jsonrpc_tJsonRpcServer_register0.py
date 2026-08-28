
# Module: ansible.utils.jsonrpc
import pytest
from ansible.utils.jsonrpc import JsonRpcServer

# Test initialization of JsonRpcServer
def test_init_JsonRpcServer():
    server = JsonRpcServer()
    assert hasattr(server, '_objects'), "The _objects attribute should be present after initialization."
    assert isinstance(server._objects, set), "The _objects attribute should be a set."