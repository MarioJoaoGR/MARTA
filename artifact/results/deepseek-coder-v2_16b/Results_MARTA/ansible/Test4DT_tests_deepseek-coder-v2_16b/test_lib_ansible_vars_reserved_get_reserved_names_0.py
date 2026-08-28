
import pytest
from ansible.vars.reserved import get_reserved_names
from ansible.playbook.base.play import Play
from ansible.playbook.role.role import Role
from ansible.playbook.block import Block
from ansible.playbook.task import Task

# Test scenario 1: test_valid_input_default_include_private
def test_valid_input_default_include_private():
    play = Play()
    role = Role()
    block = Block()
    task = Task()
    
    reserved_names = get_reserved_names()
    assert 'action' in reserved_names
    assert 'local_action' in reserved_names
    assert 'with_' in reserved_names

# Test scenario 2: test_edge_case_no_include_private
def test_edge_case_no_include_private():
    play = Play()
    role = Role()
    block = Block()
    task = Task()
    
    reserved_names = get_reserved_names(include_private=False)
    assert 'action' in reserved_names
    assert 'local_action' in reserved_names
    assert 'with_' not in reserved_names

# Test scenario 3: test_invalid_input_none
def test_invalid_input_none():
    with pytest.raises(TypeError):
        get_reserved_names(include_private=None)
