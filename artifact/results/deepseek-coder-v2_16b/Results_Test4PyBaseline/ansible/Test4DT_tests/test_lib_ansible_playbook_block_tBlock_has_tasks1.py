
import pytest
from ansible.playbook.block import Block

# Test initialization with task_include parameter
def test_init_with_task_include():
    block = Block(task_include={'tasks': [{'name': 'task1', 'action': {'module': 'foo'}}]})
    assert hasattr(block, '_parent'), "Block instance should have a _parent attribute"