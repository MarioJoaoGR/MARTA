
import pytest
import uuid
from ansible.module_utils.connection import Connection

def request_builder(method_, *args, **kwargs):
    reqid = str(uuid.uuid4())
    req = {'jsonrpc': '2.0', 'method': method_, 'id': reqid}
    req['params'] = (args, kwargs)
    return req

# Test cases for request_builder function

def test_valid_inputs():
    req = request_builder('method', 'arg1', arg2='valid')
    assert isinstance(req, dict), "Expected a dictionary"
    assert 'jsonrpc' in req, "'jsonrpc' key missing"
    assert 'method' in req, "'method' key missing"
    assert 'id' in req, "'id' key missing"
    assert 'params' in req, "'params' key missing"
    assert isinstance(req['params'], tuple), "Params should be a tuple"
    params = req['params']
    assert len(params) == 2, "Expected two elements in params"
    assert params[0] == ('arg1',), "First element of params is incorrect"
    assert params[1] == {'arg2': 'valid'}, "Second element of params is incorrect"
