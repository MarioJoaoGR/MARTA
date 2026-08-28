
import pytest
from ansible.plugins.connection.psrp import Connection


def test_invalid_inputs():
    with pytest.raises(TypeError):
        Connection(remote_addr='invalid_ip', remote_user='admin', remote_password='password')