
import pytest
from ansible.inventory.group import Group



def test_invalid_input():
    with pytest.raises(AttributeError):
        Group().test_invalid_inputs()