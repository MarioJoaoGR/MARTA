
import pytest
from ansible.inventory.group import Group


def test_invalid_input_set_variable():
    with pytest.raises(TypeError):
        Group().set_variable()