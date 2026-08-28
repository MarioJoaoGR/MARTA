
import pytest
from ansible.playbook.block import Block

# Test for valid case with a parent include task
def test_valid_case():
    block = Block(play={'name': 'example_play'}, role='admin', task_include=['task1', 'task2'], use_handlers=True, implicit=False)
    first_include = block.get_first_parent_include()
    assert isinstance(first_include, list), "Expected a list of tasks"
    assert len(first_include) == 2, "Expected two tasks in the include list"

# Test for edge case with no parent include task
def test_edge_case():
    block = Block(play={'name': 'example_play'}, role='admin', use_handlers=True, implicit=False)
    first_include = block.get_first_parent_include()
    assert first_include is None, "Expected no parent include task"

# Test for error case with invalid input
def test_error_case():
    with pytest.raises(TypeError):
        Block(invalid_input={})
