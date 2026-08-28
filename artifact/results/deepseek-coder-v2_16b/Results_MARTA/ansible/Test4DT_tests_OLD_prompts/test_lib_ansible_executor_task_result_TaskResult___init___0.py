
import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.task_result import TaskResult
from ansible.parsing.dataloader import DataLoader

def test_valid_input():
    with patch('ansible.parsing.dataloader.DataLoader') as mock_loader:
        mock_loader.return_value = MagicMock()
        return_data = {'results': [{'skipped': True}, {'skipped': False}]}
        task_fields = {'additional_field': 'value'}
        result = TaskResult(host='localhost', task='update_packages', return_data=return_data, task_fields=task_fields)
        assert result._host == 'localhost'
        assert result._task == 'update_packages'
        assert result._result == return_data
        assert result._task_fields == task_fields

def test_invalid_input():
    with pytest.raises(TypeError):
        TaskResult(host='localhost', task='update_packages', return_data=123)

def test_none_input():
    with pytest.raises(TypeError):
        TaskResult(host='localhost', task='update_packages', return_data=None)
