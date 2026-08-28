
import pytest
from ansible.playbook.included_file import IncludedFile
from ansible.playbook.task import Task

# Helper function to create a minimal instance of Task for testing
def create_minimal_task():
    return Task()

@pytest.fixture
def file1():
    return IncludedFile("example_file.txt", {"arg1": "value1"}, {"var1": "value1"}, create_minimal_task())

@pytest.fixture
def file2():
    return IncludedFile("example_file.txt", {"arg1": "value1"}, {"var1": "value1"}, create_minimal_task())

@pytest.fixture
def different_task():
    task = Task()
    task._uuid = "different-uuid"
    return IncludedFile("example_file.txt", {"arg1": "value1"}, {"var1": "value1"}, task)

@pytest.fixture
def different_parent_task():
    parent_task = Task()
    parent_task._uuid = "different-parent-uuid"
    task = Task(parent=parent_task)
    return IncludedFile("example_file.txt", {"arg1": "value1"}, {"var1": "value1"}, task)


def test_neq_different_task_uuid(file1, different_task):
    assert not (file1 == different_task)
