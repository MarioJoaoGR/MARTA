
import pytest
from ansible.plugins.connection.psrp import Connection


def test_invalid_case():
    with pytest.raises(TypeError):
        conn = Connection()