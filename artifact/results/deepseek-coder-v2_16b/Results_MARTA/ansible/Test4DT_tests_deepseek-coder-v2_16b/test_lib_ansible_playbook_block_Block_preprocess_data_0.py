
import pytest
from ansible.playbook.block import Block

def test_preprocess_data_with_simple_task():
    block = Block()
    simple_task = {'action': 'shell', 'args': {'cmd': 'echo Hello, World!'}}
    result = block.preprocess_data(simple_task)
    assert isinstance(result['block'], list), "Expected a list but got something else"
    assert len(result['block']) == 1, "Expected exactly one task in the block"
    assert result['block'][0] == simple_task, "The preprocessed data does not match the input task"


def test_preprocess_data_with_list_of_tasks():
    block = Block()
    tasks_list = [
        {'action': 'shell', 'args': {'cmd': 'echo Task 1'}},
        {'action': 'shell', 'args': {'cmd': 'echo Task 2'}}
    ]
    result = block.preprocess_data(tasks_list)
    assert isinstance(result['block'], list), "Expected a list but got something else"
    assert result['block'] == tasks_list, "The preprocessed data does not match the input list of tasks"

def test_preprocess_data_with_full_block_structure():
    block = Block()
    full_block_structure = {
        'block': [{'action': 'shell', 'args': {'cmd': 'echo Hello, World!'}}],
        'rescue': [],
        'always': []
    }
    result = block.preprocess_data(full_block_structure)
    assert isinstance(result['block'], list), "Expected a list but got something else"
    assert result['block'] == full_block_structure['block'], "The preprocessed data does not match the input full block structure"