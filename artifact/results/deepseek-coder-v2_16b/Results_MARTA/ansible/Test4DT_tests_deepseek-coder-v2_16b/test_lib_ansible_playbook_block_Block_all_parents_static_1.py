
import pytest
from ansible.playbook.block import Block
from ansible.playbook.task_include import TaskInclude

# Test fixture to create a statically loaded TaskInclude for testing
@pytest.fixture
def setup_statically_loaded_task_include():
    task_include = TaskInclude()
    task_include.statically_loaded = True
    return task_include

# Test that checks if all parents are statically loaded when the parent is a statically loaded TaskInclude
def test_all_parents_static_with_statically_loaded_parent(setup_statically_loaded_task_include):
    task_include = setup_statically_loaded_task_include
    block = Block(task_include=task_include)
    assert block.all_parents_static(), "All parents should be statically loaded since the parent is a statically loaded TaskInclude"

# Test that checks if all parents are statically loaded when there are no parents
def test_all_parents_static_with_no_parent():
    block = Block()
    assert block.all_parents_static(), "All parents should be statically loaded since there are no parents"
