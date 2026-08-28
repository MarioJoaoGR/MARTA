
import pytest
from ansible.playbook.block import Block

# Test case for initializing a Block instance with play, role, and task_include parameters
def test_block_init_with_parameters():
    block = Block(play={'name': 'example_play'}, role='admin', task_include='included_tasks')
    assert block._play == {'name': 'example_play'}
    assert block._role == 'admin'
    assert isinstance(block._parent, str)  # Assuming _parent should be a string when deserialized from parent key

# Test case for initializing a Block instance without any specific tasks or handlers
def test_block_init_without_parameters():
    block = Block(play={'name': 'another_play'})
    assert block._play == {'name': 'another_play'}
    assert block._role is None