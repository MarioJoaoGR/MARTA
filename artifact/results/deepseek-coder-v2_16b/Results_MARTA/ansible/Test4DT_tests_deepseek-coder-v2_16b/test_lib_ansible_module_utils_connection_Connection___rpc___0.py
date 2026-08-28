
import pytest
from ansible.module_utils.connection import Connection, ConnectionError

def test_invalid_input():
    conn = Connection('/tmp/socket')
    try:
        response = conn.__rpc__('subtract', 5, 'three')
    except ConnectionError as e:
        assert str(e) == "socket path /tmp/socket does not exist or cannot be found. See Troubleshooting socket path issues in the Network Debug and Troubleshooting Guide"
