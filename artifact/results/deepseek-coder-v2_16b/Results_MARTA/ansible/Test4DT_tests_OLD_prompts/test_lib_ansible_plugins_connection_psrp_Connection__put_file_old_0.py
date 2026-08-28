
import pytest
from ansible.plugins.connection.psrp import Connection

def test_valid_input():
    with pytest.raises(TypeError):
        conn = Connection()
