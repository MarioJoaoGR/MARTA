
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.connection.paramiko_ssh import Connection



def test_invalid_input():
    with pytest.raises(TypeError):
        # No patching here as we are testing the absence of an attribute
        conn = Connection()