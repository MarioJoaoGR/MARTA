
import pytest
from ansible.module_utils.connection import Connection

def test_invalid_input():
    with pytest.raises(AssertionError) as excinfo:
        conn = Connection(None)
    assert str(excinfo.value) == 'socket_path must be a value'
