
import pytest
from ansible.playbook.task import Task
from ansible.playbook.task_include import TaskInclude

# Scenario 1: Test standard input with valid TaskInclude object
def test_valid_input_happy_path():
    # Arrange
    included_task = TaskInclude(source='included_task.yml')
    main_task = Task(task_include=included_task)
    
    # Act & Assert
    assert main_task._parent is included_task
    assert main_task.get_first_parent_include() == included_task

# Scenario 2: Test edge case where _parent is None
def test_edge_case_none():
    # Arrange
    task = Task()
    
    # Act & Assert
    assert task._parent is None
    assert task.get_first_parent_include() is None

# Scenario 3: Test invalid input handling, e.g., passing a non-TaskInclude object as task_include
def test_invalid_input_error_handling():
    # Arrange
    with pytest.raises(TypeError):
        Task(task_include="not_a_valid_type")
