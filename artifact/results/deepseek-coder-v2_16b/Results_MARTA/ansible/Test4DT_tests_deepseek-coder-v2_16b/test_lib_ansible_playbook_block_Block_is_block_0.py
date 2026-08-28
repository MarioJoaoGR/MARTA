
import pytest
from ansible.playbook.block import Block

def test_valid_block():
    block = Block(play={'name': 'example_play'}, role='admin', task_include=['task1', 'task2'], use_handlers=True, implicit=False)
    assert isinstance(block, Block), "Expected an instance of Block"
