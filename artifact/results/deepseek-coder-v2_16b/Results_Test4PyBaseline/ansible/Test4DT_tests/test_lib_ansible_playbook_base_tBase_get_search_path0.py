
# Module: ansible.playbook.base
# test_base.py
from ansible.playbook.base import Base  # Corrected import statement
import os

def test_get_search_path():
    base = Base()
    # Test when dep_chain is empty
    assert base.get_search_path() == [os.path.dirname(base.get_path())]

    # Add a mock get_dep_chain method to simulate dependency chain
    def mock_get_dep_chain():
        class Role:
            _role_path = "mock_role_path"
        return [Role()]
    base.get_dep_chain = mock_get_dep_chain  # Corrected assignment

    # Test when dep_chain is not empty
    expected_path_stack = ["mock_role_path", os.path.dirname(base.get_path())]
    assert base.get_search_path() == expected_path_stack

    # Add the task directory to path_stack to simulate it being already in the list
    base._task_dir = "mock_task_dir"
    assert base.get_search_path() == ["mock_role_path", "mock_task_dir"]
