
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.jsonrpc import JsonRpcServer

def test_JsonRpcServer_invalid_params_basic():
    server = JsonRpcServer()
    
    with patch('ansible.utils.jsonrpc.JsonRpcServer.error', return_value={'jsonrpc': '2.0', 'error': {'code': -32602, 'message': 'Invalid params'}}):
        response = server.invalid_params()
        
        assert response == {'jsonrpc': '2.0', 'error': {'code': -32602, 'message': 'Invalid params'}}
