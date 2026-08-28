
import pytest
from ansible.executor.process.worker import WorkerProcess
from queue import Queue
from unittest.mock import patch, MagicMock

@pytest.fixture
def setup_worker():
    task_vars = {'key': 'value'}
    host = 'localhost'
    task = {'name': 'example_task', 'args': {}}
    play_context = {}
    loader = MagicMock()
    variable_manager = MagicMock()
    shared_loader_obj = MagicMock()
    
    worker = WorkerProcess(final_q=Queue(), task_vars=task_vars, host=host, task=task, play_context=play_context, loader=loader, variable_manager=variable_manager, shared_loader_obj=shared_loader_obj)
    return worker

def test_worker_process_initialization(setup_worker):
    worker = setup_worker
    assert isinstance(worker, WorkerProcess)
    assert worker._final_q is not None
    assert worker._task_vars == {'key': 'value'}
    assert worker._host == 'localhost'
    assert worker._task == {'name': 'example_task', 'args': {}}
    assert worker._play_context == {}
    assert worker._loader is not None
    assert worker._variable_manager is not None
    assert worker._shared_loader_obj is not None

def test_clean_up_method(setup_worker):
    worker = setup_worker
    with patch.object(worker._loader, 'cleanup_all_tmp_files') as mock_cleanup:
        mock_cleanup.return_value = True
        worker._clean_up()
        assert mock_cleanup.called
