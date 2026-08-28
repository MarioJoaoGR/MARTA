
import pytest
from ansible.playbook.block import Block

# Test preprocess_data with a non-block input that should be converted into a list
def test_preprocess_data_non_block():
    block = Block()
    example_task = {'foo': 'bar'}
    processed_task = block.preprocess_data(example_task)
    assert processed_task == {'block': [{'foo': 'bar'}]}

# Test preprocess_data with a list of tasks that should be converted into a list within the block key
def test_preprocess_data_list_of_tasks():
    block = Block()
    another_list = [{'baz': 'qux'}]
    processed_tasks = block.preprocess_data(another_list)
    assert processed_tasks == {'block': [{'baz': 'qux'}]}

# Test preprocess_data with a dictionary that should be converted into a list within the block key
def test_preprocess_data_task_dict():
    block = Block()
    task_dict = {
        'tasks': [
            {'name': 'task1', 'action': {'module': 'foo'}}
        ]
    }
    processed_dict = block.preprocess_data(task_dict)