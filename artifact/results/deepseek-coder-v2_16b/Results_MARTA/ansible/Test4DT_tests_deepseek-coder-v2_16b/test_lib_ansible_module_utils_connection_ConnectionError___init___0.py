
import pytest
from ansible.module_utils.connection import ConnectionError

def test_valid_input():
    try:
        raise ConnectionError("Failed to establish a connection.")
    except ConnectionError as e:
        assert str(e) == "Failed to establish a connection."

def test_invalid_input():
    with pytest.raises(TypeError):
        # This should raise TypeError because the constructor expects only one argument (message)
        ConnectionError()
