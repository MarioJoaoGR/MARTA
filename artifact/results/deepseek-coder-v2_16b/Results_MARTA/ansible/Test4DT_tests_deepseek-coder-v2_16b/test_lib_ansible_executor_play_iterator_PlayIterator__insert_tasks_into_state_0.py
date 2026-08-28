
import pytest
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
from ansible.executor.play_iterator import PlayIterator


def test_invalid_inputs():
    with pytest.raises(TypeError):
        PlayIterator()

