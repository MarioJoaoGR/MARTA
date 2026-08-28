
import pytest
from ansible.plugins.connection.psrp import Connection


def test_invalid_input():
    with pytest.raises(TypeError):
        # Attempting to create a Connection object without any arguments should raise TypeError
        conn = Connection()