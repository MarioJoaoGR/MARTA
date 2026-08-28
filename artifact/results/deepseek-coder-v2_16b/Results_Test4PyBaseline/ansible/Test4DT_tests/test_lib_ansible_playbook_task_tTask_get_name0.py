
# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task
import pytest

@pytest.fixture
def empty_task():
    return Task()

@pytest.fixture
def task_with_role(request):
    role = request.param
    return Task(role=role)

@pytest.fixture
def task_with_block(request):
    block = request.param
    return Task(block=block, role='exampleRole')

@pytest.fixture
def task_with_include(request):
    include_task = Task()
    return Task(task_include=include_task)

# Test cases for Task class initialization
@pytest.mark.parametrize("task_with_role", ["exampleRole"], indirect=["task_with_role"])
def test_task_initialization_with_role(task_with_role):
    assert task_with_role._role == "exampleRole"
    assert task_with_role._parent is None

@pytest.mark.parametrize("task_with_include", [], indirect=["task_with_include"])
def test_task_initialization_with_include(task_with_include):
    assert task_with_include._parent is not None

@pytest.mark.parametrize("task_with_block", [{"key": "value"}], indirect=["task_with_block"])
def test_task_initialization_with_block(task_with_block):
    assert task_with_block._parent == {"key": "value"}

# Test cases for get_name method
@pytest.mark.parametrize("task_with_role", ["exampleRole"], indirect=["task_with_role"])
def test_get_name_with_role(task_with_role):
    assert task_with_role.get_name() == "exampleRole : None"

@pytest.mark.parametrize("task_with_block", [{"key": "value"}], indirect=["task_with_block"])
def test_get_name_with_block(task_with_block):
    assert task_with_block.get_name() == "None : None"

@pytest.mark.parametrize("task_with_role", ["exampleRole"], indirect=["task_with_role"])
def test_get_name_include_fqcn(task_with_role):
    assert task_with_role.get_name(include_role_fqcn=True) == "exampleRole : None"
