
import pytest
from ansible.inventory.host import Host


def test_invalid_input_error_handling():
    with pytest.raises(ValueError):
        raise ValueError("This is a test error")