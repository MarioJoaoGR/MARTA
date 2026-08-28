
import pytest
from queue import Queue
from ansible.executor.process.worker import WorkerProcess
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager



def test_tempfiles_attribute():
    final_q = Queue()
    task_vars = {'key': 'value'}
    host = 'localhost'
    task = {'name': 'example_task', 'args': {}}
    play_context = {}
    loader = DataLoader()
    variable_manager = VariableManager()
    shared_loader_obj = DataLoader()
    
    worker = WorkerProcess(final_q, task_vars, host, task, play_context, loader, variable_manager, shared_loader_obj)
    
    assert hasattr(worker._loader, '_tempfiles'), "Expected _tempfiles attribute to be present"
    assert isinstance(worker._loader._tempfiles, set), "_tempfiles should be a set"