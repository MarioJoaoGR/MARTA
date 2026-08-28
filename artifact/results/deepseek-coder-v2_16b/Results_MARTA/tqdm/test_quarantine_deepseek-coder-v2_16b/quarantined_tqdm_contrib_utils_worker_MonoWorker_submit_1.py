
import pytest
from tqdm.contrib.utils_worker import MonoWorker
from concurrent.futures import Future
import time

@pytest.fixture(scope="module")
def mono_worker():
    return MonoWorker()


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker_submit_1.py F [ 50%]
Another task
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

mono_worker = <tqdm.contrib.utils_worker.MonoWorker object at 0x7f2a7e0de7a0>

    def test_valid_input(mono_worker):
        def example_task():
            print("Task is running")
    
        # Submit a task
        future = mono_worker.submit(example_task)
        assert isinstance(future, Future)
>       assert future._state == 'running' or future._state == 'finished'
E       AssertionError: assert ('RUNNING' == 'running'
E         
E         - running
E         + RUNNING or 'RUNNING' == 'finished'
E         
E         - finished
E         + RUNNING)

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker_submit_1.py:18: AssertionError
----------------------------- Captured stdout call -----------------------------
Task is running
--------------------------- Captured stdout teardown ---------------------------

________________________________ test_edge_case ________________________________

mono_worker = <tqdm.contrib.utils_worker.MonoWorker object at 0x7f2a7e0de7a0>

    def test_edge_case(mono_worker):
        def example_task():
            print("Task is running")
    
        # Submit a task immediately
        mono_worker.submit(example_task)
        time.sleep(1)  # Wait for the task to complete
    
        # Try submitting another task, it should run immediately without waiting
        future = mono_worker.submit(lambda: print("Another task"))
        assert isinstance(future, Future)
>       assert future._state == 'running' or future._state == 'finished'
E       AssertionError: assert ('PENDING' == 'running'
E         
E         - running
E         + PENDING or 'PENDING' == 'finished'
E         
E         - finished
E         + PENDING)

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker_submit_1.py:31: AssertionError
----------------------------- Captured stdout call -----------------------------
Task is running
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker_submit_1.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_utils_worker_MonoWorker_submit_1.py::test_edge_case
============================== 2 failed in 1.06s ===============================
"""