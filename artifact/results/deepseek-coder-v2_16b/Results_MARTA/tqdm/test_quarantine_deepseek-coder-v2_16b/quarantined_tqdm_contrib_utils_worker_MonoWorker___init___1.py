
import pytest
from concurrent.futures import ThreadPoolExecutor, Future
from collections import deque
import time

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
        future = self.pool.submit(task)
        if len(self.futures) >= 2:
            self.futures.pop()
        self.futures.appendleft(future)
        return future

# Test cases for MonoWorker class


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker___init___1.py Task 2
F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________ test_mono_worker_runs_latest_task _______________________

    def test_mono_worker_runs_latest_task():
        mono_worker = MonoWorker()
    
        # Submit the first task
        future1 = mono_worker.submit(lambda: print("Task 1"))
    
        # Wait a bit to ensure the task is running
        time.sleep(0.5)
    
        # Submit the second task
        future2 = mono_worker.submit(lambda: print("Task 2"))
    
        # Ensure the first task is not running anymore (discarded)
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker___init___1.py:58: Failed
----------------------------- Captured stdout call -----------------------------
Task 1
___________________ test_mono_worker_handles_multiple_tasks ____________________

    def test_mono_worker_handles_multiple_tasks():
        mono_worker = MonoWorker()
    
        # Submit the first task
        future1 = mono_worker.submit(lambda: time.sleep(1))
    
        # Wait a bit to ensure the first task is running
        time.sleep(0.5)
    
        # Submit the second task
        future2 = mono_worker.submit(lambda: print("Task 2"))
    
        # Ensure the first task is not running anymore (discarded)
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker___init___1.py:78: Failed
----------------------------- Captured stdout call -----------------------------
Task 2
--------------------------- Captured stdout teardown ---------------------------

_____________________ test_mono_worker_limits_to_two_tasks _____________________

    def test_mono_worker_limits_to_two_tasks():
        mono_worker = MonoWorker()
    
        # Submit the first task
        future1 = mono_worker.submit(lambda: time.sleep(1))
    
        # Wait a bit to ensure the first task is running
        time.sleep(0.5)
    
        # Submit the second task
        future2 = mono_worker.submit(lambda: print("Task 2"))
    
        # Ensure the first task is not running anymore (discarded)
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker___init___1.py:98: Failed
----------------------------- Captured stdout call -----------------------------
ask 2
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker___init___1.py::test_mono_worker_runs_latest_task
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker___init___1.py::test_mono_worker_handles_multiple_tasks
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker___init___1.py::test_mono_worker_limits_to_two_tasks
============================== 3 failed in 2.55s ===============================
"""