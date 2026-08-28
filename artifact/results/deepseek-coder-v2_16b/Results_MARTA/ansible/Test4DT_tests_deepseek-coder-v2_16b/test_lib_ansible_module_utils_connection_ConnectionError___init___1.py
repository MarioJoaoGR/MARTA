
import pytest
from ansible.module_utils.connection import ConnectionError

def test_edge_case():
    with pytest.raises(ConnectionError) as exc_info:
        raise ConnectionError("Failed to establish a connection.")
    assert str(exc_info.value) == "Failed to establish a connection."
