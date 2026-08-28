
import pytest
from ansible.module_utils.connection import Connection

def test_error_handling():
    with pytest.raises(AssertionError):
        conn = Connection(None)
