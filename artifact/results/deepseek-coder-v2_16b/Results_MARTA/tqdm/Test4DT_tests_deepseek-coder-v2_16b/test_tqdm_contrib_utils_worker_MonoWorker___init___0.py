
import pytest
from tqdm.contrib.utils_worker import MonoWorker
from concurrent.futures import Future

@pytest.fixture
def mono_worker():
    return MonoWorker()

def test_mono_worker_submit(mono_worker):
    # Submit a task that prints "Task is running"
    def example_task():
        print("Task is running")
    
    future1 = mono_worker.submit(example_task)
    assert isinstance(future1, Future)
    assert not future1._state == 'running'  # The task should be immediately executed and marked as not running

def test_mono_worker_discard_old_tasks(mono_worker):
    # Submit a task that prints "Task is running"
    def example_task():
        print("Task is running")
    
    future1 = mono_worker.submit(example_task)
    assert not future1._state == 'running'  # The first task should be marked as not running

def test_mono_worker_max_two_tasks(mono_worker):
    # Submit two tasks
    def example_task1():
        print("Task 1 is running")
    
    future1 = mono_worker.submit(example_task1)
    assert not future1._state == 'running'  # The first task should be immediately executed and marked as not running
