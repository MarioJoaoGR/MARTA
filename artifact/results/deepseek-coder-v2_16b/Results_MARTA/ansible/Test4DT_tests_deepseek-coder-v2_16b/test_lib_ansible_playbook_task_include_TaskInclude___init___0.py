
import pytest
from lib.ansible.playbook.task_include import TaskInclude

# Test scenario 1: Basic Usage
def test_basic_usage():
    block = {
        'file': 'path/to/task',
        '_raw_params': {'action': 'some_action', 'args': {'arg1': 'value1'}}
    }
    role = 'include'
    task_include = {}
    
    task_include_instance = TaskInclude(block=block, role=role, task_include=task_include)
    assert hasattr(task_include_instance, 'statically_loaded'), "TaskInclude instance should have a statically_loaded attribute"

# Test scenario 2: Including a Task with Additional Parameters
def test_additional_parameters():
    block = {
        'file': 'path/to/another_task',
        '_raw_params': {'action': 'another_action', 'args': {'arg2': 'value2'}}
    }
    role = 'include'
    task_include = {}
    
    task_include_instance = TaskInclude(block=block, role=role, task_include=task_include)
    assert hasattr(task_include_instance, 'statically_loaded'), "TaskInclude instance should have a statically_loaded attribute"

# Test scenario 3: Including a Task from a File
def test_including_from_file():
    block = None
    role = 'include'
    task_include = {'file': 'path/to/included_task_file.yml'}
    
    task_include_instance = TaskInclude(block=block, role=role, task_include=task_include)
    assert hasattr(task_include_instance, 'statically_loaded'), "TaskInclude instance should have a statically_loaded attribute"

# Test scenario 4: Including a Task with Role and Action Specified
def test_specified_role_and_action():
    block = {
        'file': None,
        '_raw_params': {'action': 'some_role::some_action', 'args': {'arg1': 'value1'}}
    }
    role = None
    task_include = {}
    
    task_include_instance = TaskInclude(block=block, role=role, task_include=task_include)
    assert hasattr(task_include_instance, 'statically_loaded'), "TaskInclude instance should have a statically_loaded attribute"

# Test scenario 5: Including a Task with No Parameters Specified
def test_no_parameters_specified():
    block = None
    role = 'include'
    task_include = {}
    
    task_include_instance = TaskInclude(block=block, role=role, task_include=task_include)
    assert hasattr(task_include_instance, 'statically_loaded'), "TaskInclude instance should have a statically_loaded attribute"
