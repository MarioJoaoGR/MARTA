
import pytest
from ansible.playbook.block import Block
from ansible.parsing.dataloader import DataLoader

# Test initialization of Block with various parameters
def test_block_initialization():
    block = Block(play={'name': 'example_play'}, role='admin', task_include='included_tasks')
    assert block._play == {'name': 'example_play'}
    assert block._role == 'admin'
    assert block._parent == 'included_tasks'

# Test initialization of Block without specific tasks or handlers
def test_block_initialization_without_specifics():
    block = Block(play={'name': 'another_play'})
    assert block._play == {'name': 'another_play'}
    assert block._role is None