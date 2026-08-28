
import pytest
from ansible.inventory.group import Group



def test_silent_mode_keeps_original_name():
    with pytest.raises(TypeError):
        group = Group(name="my-group!name", silent=True)