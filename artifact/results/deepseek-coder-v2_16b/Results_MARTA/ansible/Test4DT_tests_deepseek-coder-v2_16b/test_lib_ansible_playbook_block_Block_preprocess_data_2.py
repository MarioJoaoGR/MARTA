
import pytest
from ansible.playbook.block import Block

def test_preprocess_data_simple_task():
    block = Block()
    simple_task = {'action': 'shell', 'args': {'cmd': 'echo Hello, World!'}}
    result = block.preprocess_data(simple_task)
    assert isinstance(result['block'], list)
    assert len(result['block']) == 1
    assert result['block'][0] == simple_task

def test_preprocess_data_full_block():
    block = Block()
    full_block_structure = {
        'block': [{'action': 'shell', 'args': {'cmd': 'echo Hello, World!'}}],
        'rescue': [],
        'always': []
    }
    result = block.preprocess_data(full_block_structure)
    assert isinstance(result['block'], list)
    assert len(result['block']) == 1
    assert result['block'][0] == full_block_structure['block'][0]

def test_preprocess_data_tasks_list():
    block = Block()
    tasks_list = [
        {'action': 'shell', 'args': {'cmd': 'echo Task 1'}},
        {'action': 'shell', 'args': {'cmd': 'echo Task 2'}}
    ]
    result = block.preprocess_data(tasks_list)
    assert isinstance(result['block'], list)
    assert len(result['block']) == 2
    assert result['block'] == tasks_list
