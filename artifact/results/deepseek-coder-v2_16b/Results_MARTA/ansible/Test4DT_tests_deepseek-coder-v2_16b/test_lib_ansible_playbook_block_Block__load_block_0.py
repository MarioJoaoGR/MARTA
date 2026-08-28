
import pytest
from ansible.playbook.block import Block
from ansible.errors import AnsibleParserError

# Test valid input scenario
def test_valid_input():
    ds = {'tasks': ['task1', 'task2']}
    block = Block()
    result = block._load_block('_block', ds)
    assert isinstance(result, list), "Expected a list of tasks"
    assert len(result) == 2, "Expected two tasks in the block"
    assert all(isinstance(task, str) for task in result), "All tasks should be strings"

# Test edge case scenario with None input
def test_edge_case():
    ds = None
    block = Block()
    with pytest.raises(AnsibleParserError):
        block._load_block('_block', ds)

# Test invalid input scenario
def test_invalid_input():
    ds = {'tasks': 'not a list'}
    block = Block()
    with pytest.raises(AnsibleParserError):
        block._load_block('_block', ds)
