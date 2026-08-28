
import pytest
from ansible.inventory.host import Host

def test_invalid_inputs():
    with pytest.raises(ValueError):
        Host(name=123, port='port', gen_uuid=True)
