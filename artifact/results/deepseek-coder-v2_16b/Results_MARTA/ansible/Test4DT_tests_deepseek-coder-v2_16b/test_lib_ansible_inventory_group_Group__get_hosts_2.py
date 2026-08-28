
import pytest
from ansible.inventory.group import Group

def test_invalid_characters_in_name():
    with pytest.raises(TypeError):
        g = Group(name="my-group!name", force=True)

def test_silent_option_with_invalid_characters():
    with pytest.raises(TypeError):
        g = Group(name="my-group!name", silent=True)
