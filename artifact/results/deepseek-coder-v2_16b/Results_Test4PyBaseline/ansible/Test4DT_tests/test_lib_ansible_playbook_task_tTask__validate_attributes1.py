
# Module: ansible.playbook.task
# test_task.py
from ansible.errors import AnsibleParserError
import pytest
from ansible.playbook.task import Task

@pytest.fixture
def default_task():
    return Task()

@pytest.fixture
def task_with_invalid_attribute():
    # Creating a dictionary with an invalid attribute to trigger validation error
    ds = {'invalid_attr': 'value'}
    task = Task()
    with pytest.raises(AnsibleParserError):
        task._validate_attributes(ds)  # This should raise an exception
    return task

@pytest.fixture
def task_with_valid_attribute():
    ds = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    task = Task()
    task._validate_attributes(ds)  # This should not raise an exception
    return task

def test_default_task(default_task):
    assert default_task._role is None
    assert default_task._parent is None
    assert not default_task.implicit
    assert default_task.resolved_action is None

def test_task_with_invalid_attribute(task_with_invalid_attribute):
    with pytest.raises(AnsibleParserError) as exc_info:
        task_with_invalid_attribute._validate_attributes({'invalid_attr': 'value'})
    assert "is not a valid attribute for a Task" in str(exc_info.value)

def test_task_with_valid_attribute(task_with_valid_attribute):
    task_with_valid_attribute._validate_attributes({'action': 'shell', 'args': {'cmd': 'echo hello'}})
    assert True  # No exception should be raised if the attributes are valid

def test_preprocess_data_invalid(default_task):
    ds = {'key': 'value'}
    with pytest.raises(AnsibleParserError) as exc_info:
        default_task.preprocess_data(ds)