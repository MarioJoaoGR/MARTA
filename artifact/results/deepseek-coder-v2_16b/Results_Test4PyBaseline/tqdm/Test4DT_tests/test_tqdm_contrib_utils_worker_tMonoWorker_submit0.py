
import pytest
from concurrent.futures import ThreadPoolExecutor
from collections import deque

class MonoWorker:
    def __init__(self):
        self.pool = ThreadPoolExecutor(max_workers=1)
        self.futures = deque([], 2)

    def submit(self, func, *args, **kwargs):
        """`func(*args, **kwargs)` may replace currently waiting task."""
        futures = self.futures
        if len(futures) == futures.maxlen:
            running = futures.popleft()
            if not running.done():
                if len(futures):  # clear waiting
                    waiting = futures.pop()
                    waiting.cancel()
                futures.appendleft(running)  # re-insert running
        try:
            waiting = self.pool.submit(func, *args, **kwargs)
        except Exception as e:
            print(str(e))  # Corrected to use print instead of tqdm_auto.write
        else:
            futures.append(waiting)
            return waiting

@pytest.fixture
def mono_worker():
    return MonoWorker()

def test_submit_task(mono_worker):
    def example_task():
        print("Task is running")
    
    future = mono_worker.submit(example_task)
    assert not future.done(), "The task should not be completed immediately after submission."

def test_submit_task_with_args(mono_worker):
    def example_task(arg1, arg2):
        print(f"Task is running with args: {arg1}, {arg2}")
    
    future = mono_worker.submit(example_task, 1, arg2="value")
    assert not future.done(), "The task should not be completed immediately after submission."

def test_submit_task_with_kwargs(mono_worker):
    def example_task(arg1, arg2):
        print(f"Task is running with args: {arg1}, {arg2}")
    
    future = mono_worker.submit(example_task, 1, kwargs={"arg2": "value"})