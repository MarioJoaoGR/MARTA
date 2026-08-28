
import pytest
from ansible.executor.task_result import TaskResult


def test_edge_case_none():
    with pytest.raises(TypeError):
        TaskResult(host='localhost', task='example_task', return_data=None)