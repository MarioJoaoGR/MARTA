
import pytest
from ansible.module_utils.connection import Connection

def test_valid_input():
    conn = Connection('/tmp/socket')
    assert conn.socket_path == '/tmp/socket'

def test_none_input():
    with pytest.raises(AssertionError) as e:
        conn = Connection(None)
    assert str(e.value) == 'socket_path must be a value'

def test_invalid_method():
    conn = Connection('/tmp/socket')
    with pytest.raises(Exception):
        response = conn.__rpc__('nonexistentMethod', 'arg1', arg2='value2')
