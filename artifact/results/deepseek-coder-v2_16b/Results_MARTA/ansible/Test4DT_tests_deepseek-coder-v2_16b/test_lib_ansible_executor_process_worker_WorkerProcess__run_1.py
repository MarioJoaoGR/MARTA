
import pytest
from ansible.executor.process.worker import WorkerProcess
from queue import Queue
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

def test_valid_init():
    final_q = Queue()
    task_vars = {'key': 'value'}
    host = 'localhost'
    task = {'name': 'example_task', 'args': {}}
    play_context = {}
    loader = DataLoader()
    variable_manager = VariableManager()
    shared_loader_obj = DataLoader()
    
    worker = WorkerProcess(final_q=final_q, task_vars=task_vars, host=host, task=task, play_context=play_context, loader=loader, variable_manager=variable_manager, shared_loader_obj=shared_loader_obj)
    
    assert worker._final_q == final_q
    assert worker._task_vars == task_vars
    assert worker._host == host
    assert worker._task == task
    assert worker._play_context == play_context
    assert isinstance(worker._loader, DataLoader)
    assert isinstance(worker._variable_manager, VariableManager)
    assert isinstance(worker._shared_loader_obj, DataLoader)
