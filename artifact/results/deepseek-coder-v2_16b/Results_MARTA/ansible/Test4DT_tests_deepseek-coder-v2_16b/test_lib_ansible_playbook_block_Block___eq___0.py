
import pytest
from ansible.playbook.block import Block

def test_block_creation():
    block = Block(play={'name': 'example_play'}, role='admin', task_include=['task1', 'task2'], use_handlers=True, implicit=False)
    assert isinstance(block, Block), "Block instance should be an instance of the Block class"
    assert len(block._parent) == 2, "Expected two tasks to be included in the block"
