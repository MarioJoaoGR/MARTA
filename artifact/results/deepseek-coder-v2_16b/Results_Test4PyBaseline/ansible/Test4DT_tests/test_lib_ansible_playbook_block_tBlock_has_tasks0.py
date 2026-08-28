
import pytest
from ansible.playbook.block import Block

# Test initialization with task_include parameter
def test_init_with_task_include():
    block = Block(task_include={'tasks': [{'name': 'task1', 'action': {'module': 'foo'}}]})
    assert hasattr(block, '_parent'), "Block instance should have a _parent attribute"
    assert len(block._block) == 1, "Block instance should have one task after initialization with task_include"

# Test initialization without parameters
def test_init_without_parameters():
    block = Block()
    assert not hasattr(block, '_parent'), "Block instance should not have a _parent attribute if not provided"
    assert len(block._block) == 0, "Block instance should have no tasks initially"

# Test initialization with play and role parameters
def test_init_with_play_and_role():
    block = Block(play={'name': 'example_play'}, role='admin', task_include='included_tasks')
    assert hasattr(block, '_parent'), "Block instance should have a _parent attribute"
    assert len(block._block) > 0, "Block instance should have tasks after initialization with play and role parameters"

# Test has_tasks method when no tasks are present
def test_has_tasks_no_tasks():
    block = Block()
    assert not block.has_tasks(), "has_tasks should return False if there are no tasks in the block, rescue, or always lists"

# Test has_tasks method when tasks are present
def test_has_tasks_with_tasks():
    block = Block(task_include={'tasks': [{'name': 'task1', 'action': {'module': 'foo'}}]})
    assert block.has_tasks(), "has_tasks should return True if there are tasks in the block, rescue, or always lists"

# Test has_tasks method when only one type of task is present
def test_has_tasks_one_type():
    block = Block(task_include={'tasks': [{'name': 'task1', 'action': {'module': 'foo'}}], 'rescue': [], 'always': []})
    assert block.has_tasks(), "has_tasks should return True if there are tasks in any of the block, rescue, or always lists"
