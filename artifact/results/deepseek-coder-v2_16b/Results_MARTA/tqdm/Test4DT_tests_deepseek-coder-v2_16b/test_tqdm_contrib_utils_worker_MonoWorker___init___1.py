
import pytest
from concurrent.futures import Future
from collections import deque
from tqdm.contrib.utils_worker import MonoWorker

def test_submit_valid_task():
    mono_worker = MonoWorker()
    
    def example_task():
        return "Task is running"
    
    future = mono_worker.submit(example_task)
    assert isinstance(future, Future), f"Expected a Future object but got {type(future)}"
