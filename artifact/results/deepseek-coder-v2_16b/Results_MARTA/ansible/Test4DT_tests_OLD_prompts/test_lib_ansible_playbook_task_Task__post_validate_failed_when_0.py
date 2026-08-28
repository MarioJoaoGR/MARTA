
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.task import Task

def test_valid_inputs():
    class MockTask(Task):
        pass
    
    with patch.object(MockTask, '__init__', lambda self: None):
        task_include = MagicMock()
        with pytest.raises(TypeError):
            MockTask(task_include=task_include)
