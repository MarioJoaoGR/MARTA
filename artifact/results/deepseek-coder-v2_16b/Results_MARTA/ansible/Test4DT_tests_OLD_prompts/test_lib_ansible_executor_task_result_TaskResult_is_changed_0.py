
import pytest
from unittest.mock import patch, MagicMock
from lib.ansible.executor.task_result import TaskResult

@pytest.fixture
def task_result():
    return TaskResult(host='localhost', task='update_packages', return_data={'results': [{'failed': True}, {'failed': False}]})

def test_is_changed(task_result):
    with patch('lib.ansible.executor.task_result.DataLoader') as mock_dataloader:
        mock_data = {'results': [{'changed': True}, {'changed': False}]}
        mock_instance = MagicMock()
        mock_instance.__getitem__.return_value = mock_data
        mock_dataloader.return_value.load.return_value = mock_instance

        task_result = TaskResult(host='localhost', task='update_packages', return_data=mock_data)
        assert task_result.is_changed() == True

def test_is_failed(task_result):
    with patch('lib.ansible.executor.task_result.DataLoader') as mock_dataloader:
        mock_data = {'results': [{'failed': True}, {'failed': False}]}
        mock_instance = MagicMock()
        mock_instance.__getitem__.return_value = mock_data
        mock_dataloader.return_value.load.return_value = mock_instance

        task_result = TaskResult(host='localhost', task='update_packages', return_data=mock_data)
        assert task_result.is_failed() == True

def test_is_skipped(task_result):
    with patch('lib.ansible.executor.task_result.DataLoader') as mock_dataloader:
        mock_data = {'results': [{'skipped': True}, {'skipped': False}]}
        mock_instance = MagicMock()
        mock_instance.__getitem__.return_value = mock_data
        mock_dataloader.return_value.load.return_value = mock_instance

        task_result = TaskResult(host='localhost', task='update_packages', return_data=mock_data)
        assert task_result.is_skipped() == False

def test_is_unreachable(task_result):
    with patch('lib.ansible.executor.task_result.DataLoader') as mock_dataloader:
        mock_data = {'unreachable': True}
        mock_instance = MagicMock()
        mock_instance.__getitem__.return_value = mock_data
        mock_dataloader.return_value.load.return_value = mock_instance

        task_result = TaskResult(host='localhost', task='update_packages', return_data=mock_data)
        assert task_result.is_unreachable() == True
