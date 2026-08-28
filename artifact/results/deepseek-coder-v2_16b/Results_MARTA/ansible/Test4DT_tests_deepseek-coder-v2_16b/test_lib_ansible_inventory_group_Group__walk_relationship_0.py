
import pytest
from ansible.inventory.group import Group



def test_silent_mode():
    with pytest.raises(TypeError):
        Group("my-group!name", silent=True)