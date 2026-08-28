
# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task
import pytest

def test_post_validate_changed_when():
    task = Task()
    templar = None  # Assuming templar is not used in the function, so we set it to None for simplicity
    
    # Test case where changed_when is expected to be returned without any modification
    value = "expected_value"
    result = task._post_validate_changed_when("changed_when", value, templar)
    assert result == value, f"Expected {value} but got {result}"
