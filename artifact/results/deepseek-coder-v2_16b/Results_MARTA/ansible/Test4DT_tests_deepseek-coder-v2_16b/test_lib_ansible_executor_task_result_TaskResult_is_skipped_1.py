
import pytest
from ansible.executor.task_result import TaskResult


def test_edge_case_none():
    with pytest.raises(TypeError):
        TaskResult(host='localhost', task='update_packages', return_data=None)