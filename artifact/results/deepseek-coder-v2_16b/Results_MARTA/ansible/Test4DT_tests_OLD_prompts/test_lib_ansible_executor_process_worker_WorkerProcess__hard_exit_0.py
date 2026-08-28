
import pytest
from ansible.executor.process.worker import WorkerProcess
from queue import Queue
from unittest.mock import patch, MagicMock

# Test case for the WorkerProcess class initialization
def test_worker_process_initialization():
    final_q = Queue()
    task_vars = {}
    host = 'localhost'
    task = {'name': 'example_task', 'args': {}}
    play_context = {}
    loader = MagicMock()
    variable_manager = MagicMock()
    shared_loader_obj = MagicMock()
    
    worker = WorkerProcess(final_q=final_q, task_vars=task_vars, host=host, task=task, play_context=play_context, loader=loader, variable_manager=variable_manager, shared_loader_obj=shared_loader_obj)
    
    assert worker._final_q == final_q
    assert worker._task_vars == task_vars
    assert worker._host == host
    assert worker._task == task
    assert worker._play_context == play_context
    assert worker._loader == loader
    assert worker._variable_manager == variable_manager
    assert worker._shared_loader_obj == shared_loader_obj

# Test case for the _hard_exit method
def test_worker_process_hard_exit():
    worker = WorkerProcess(final_q=Queue(), task_vars={}, host='localhost', task={'name': 'example_task', 'args': {}}, play_context={}, loader=MagicMock(), variable_manager=MagicMock(), shared_loader_obj=MagicMock())
    
    with patch('ansible.executor.process.worker.display') as mock_display:
        with patch('ansible.executor.process.worker.os._exit') as mock_exit:
            e = Exception("Test exception")
            worker._hard_exit(e)
            
            mock_display.debug.assert_called_with(f"WORKER HARD EXIT: {str(e)}")
            mock_exit.assert_called_with(1)
