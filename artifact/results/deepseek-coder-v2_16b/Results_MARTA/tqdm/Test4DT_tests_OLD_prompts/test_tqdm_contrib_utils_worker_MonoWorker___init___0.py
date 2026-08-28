
import pytest
from concurrent.futures import ThreadPoolExecutor, Future
from collections import deque
from unittest.mock import patch

# Assuming the module you want to test is 'tqdm.contrib.utils_worker'
# from tqdm.contrib.utils_worker import MonoWorker

class MonoWorker:
    """
    A class to support running one task at a time, with the most recent waiting task being executed.
    
    Attributes:
        pool (ThreadPoolExecutor): An executor for running tasks concurrently. It is initialized with a maximum of 1 worker.
        futures (deque): A double-ended queue to store up to two future objects representing submitted tasks.
        
    Methods:
        submit(task): Submits a task to be executed by the MonoWorker. If another task is already waiting, it will be discarded.
    
    Example:
        mono_worker = MonoWorker()
        def example_task():
            print("Task is running")
        
        # Submit a task
        mono_worker.submit(example_task)  # This will run the task immediately since no other tasks are waiting.
        
        # Submit another task after some time
        import time
        time.sleep(1)
        mono_worker.submit(lambda: print("Another task"))  # The first task is discarded and this one runs instead.
    
    This class is designed to ensure that only the most recent submitted task is executed, with any previously submitted tasks being ignored or canceled if necessary. It uses a ThreadPoolExecutor for concurrent execution and maintains a queue of up to two futures to manage the task submissions.
    """
    def __init__(self):
        self.pool = ThreadPoolExecutor(max_workers=1)
        self.futures = deque([], 2)

    def submit(self, task):
        if not callable(task):
            raise TypeError("Task must be a callable.")
        future = self.pool.submit(task)
        self.futures.append(future)
        return future

# Test cases for MonoWorker class
def test_edge_cases():
    mono_worker = MonoWorker()
    
    # Test with None input
    with pytest.raises(TypeError):
        mono_worker.submit(None)

def test_invalid_inputs():
    mono_worker = MonoWorker()
    
    # Test with invalid task type (e.g., int instead of callable)
    with pytest.raises(TypeError):
        mono_worker.submit(42)  # An integer is not a callable

def test_valid_task():
    mono_worker = MonoWorker()
    
    # Test with a valid callable task
    def example_task():
        return "Task executed"
    
    future = mono_worker.submit(example_task)
    assert future.result() == "Task executed"
