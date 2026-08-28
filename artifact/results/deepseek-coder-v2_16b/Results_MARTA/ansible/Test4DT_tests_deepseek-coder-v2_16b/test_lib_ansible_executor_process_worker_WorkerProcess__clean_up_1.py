
import pytest
from ansible.executor.process.worker import WorkerProcess
from queue import Queue
from unittest.mock import patch, MagicMock

# Test 1: Initialization of WorkerProcess
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

def test_initialization(worker_process):
    assert isinstance(worker_process, WorkerProcess)
    assert worker_process._final_q is not None
    assert worker_process._task_vars == {'key': 'value'}
    assert worker_process._host == 'localhost'
    assert worker_process._task == {'name': 'example_task', 'args': {}}
    assert worker_process._play_context == {}
    assert worker_process._loader is not None
    assert worker_process._variable_manager is not None
    assert worker_process._shared_loader_obj is not None

# Test 2: Clean Up Method
@pytest.fixture(scope="module")
def clean_up_worker():
    task_vars = {'key': 'value'}
    host = 'localhost'
    task = {'name': 'example_task', 'args': {}}
    play_context = {}
    loader = MagicMock()
    variable_manager = MagicMock()
    shared_loader_obj = MagicMock()
    
    worker = WorkerProcess(final_q=Queue(), task_vars=task_vars, host=host, task=task, play_context=play_context, loader=loader, variable_manager=variable_manager, shared_loader_obj=shared_loader_obj)
    return worker

def test_clean_up(clean_up_worker):
    with patch.object(clean_up_worker._loader, 'cleanup_all_tmp_files') as mock_cleanup:
        clean_up_worker._clean_up()
        mock_cleanup.assert_called_once()
