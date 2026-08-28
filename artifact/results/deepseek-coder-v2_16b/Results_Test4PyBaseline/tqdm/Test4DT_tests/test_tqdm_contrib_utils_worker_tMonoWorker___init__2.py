# Module: tqdm.contrib.utils_worker
import pytest
from concurrent.futures import ThreadPoolExecutor
from collections import deque

class MonoWorker:
    def __init__(self):
        self.pool = ThreadPoolExecutor(max_workers=1)
        self.futures = deque([], 2)

    def submit(self, func, *args, **kwargs):
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
            print(str(e))
        else:
            futures.append(waiting)
            return waiting

# Test cases for MonoWorker class
def test_basic_usage():
    def simple_task():
        print("Simple task executing")
    
    mono_worker = MonoWorker()
    future = mono_worker.submit(simple_task)
    assert future is not None, "The future should be created"

def test_with_arguments():
    def task_with_args(a, b):
        print(f"Executing with args: {a}, {b}")
    
    mono_worker = MonoWorker()
    future = mono_worker.submit(task_with_args, 1, 2)
    assert future is not None, "The future should be created"

def test_with_keyword_arguments():
    def task_with_kwargs(**kwargs):
        print(f"Executing with kwargs: {kwargs}")
    
    mono_worker = MonoWorker()
    future = mono_worker.submit(task_with_kwargs, a=1, b=2)
    assert future is not None, "The future should be created"

def test_handling_errors():
    def error_task():
        raise ValueError("An error occurred")
    
    mono_worker = MonoWorker()
    future = mono_worker.submit(error_task)
    assert future is not None, "The future should be created"

# Run the tests
if __name__ == "__main__":
    pytest.main()
