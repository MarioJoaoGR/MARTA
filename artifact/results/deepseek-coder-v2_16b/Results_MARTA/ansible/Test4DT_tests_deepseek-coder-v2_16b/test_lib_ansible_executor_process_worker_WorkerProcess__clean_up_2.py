
import pytest
from ansible.executor.process.worker import WorkerProcess
from queue import Queue
from unittest.mock import patch, MagicMock

@pytest.fixture(scope="module")
def worker_process():
    task_vars = {'key': 'value'}
    host = 'localhost'
    task = {'name': 'example_task', 'args': {}}
    play_context = {}
    loader = MagicMock()
    variable_manager = MagicMock()
    shared_loader_obj = MagicMock()
    
    worker = WorkerProcess(final_q=Queue(), task_vars=task_vars, host=host, task=task, play_context=play_context, loader=loader, variable_manager=variable_manager, shared_loader_obj=shared_loader_obj)
    return worker

def test_clean_up(worker_process):
    with patch.object(worker_process._loader, 'cleanup_all_tmp_files') as mock_cleanup:
        worker_process._clean_up()
        mock_cleanup.assert_called_once()
