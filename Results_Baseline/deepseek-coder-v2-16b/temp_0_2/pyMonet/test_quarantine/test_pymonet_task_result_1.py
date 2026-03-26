
# Module: pymonet.task
from pymonet.task import Task
import random

def handle_success(value):
    print("Success:", value)

def handle_failure(error):
    print("Failure:", error)

# Test handling a successful computation
def test_successful_computation():
    task = Task(lambda reject, resolve: resolve(42))
    task.fork(handle_failure, handle_success)

# Test handling a failing computation
def test_failing_computation():
    task = Task(lambda reject, resolve: reject("Computation failed"))
    task.fork(handle_failure, handle_success)

# Test handling a computation that might fail or succeed randomly
def test_random_computation():
    def computation():
        if random.choice([True, False]):
            return 42
        else:
            raise ValueError("Computation failed")
    
    task = Task(lambda reject, resolve: resolve(computation()) if computation() is not None else reject(computation()))
    task.fork(handle_failure, handle_success)

# Run the tests
if __name__ == "__main__":
    test_successful_computation()
    test_failing_computation()
    test_random_computation()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pyMonet/Test4DT_tests/test_pymonet_task_result_1.py ..F                  [100%]

=================================== FAILURES ===================================
___________________________ test_random_computation ____________________________

    def test_random_computation():
        def computation():
            if random.choice([True, False]):
                return 42
            else:
                raise ValueError("Computation failed")
    
        task = Task(lambda reject, resolve: resolve(computation()) if computation() is not None else reject(computation()))
>       task.fork(handle_failure, handle_success)

pyMonet/Test4DT_tests/test_pymonet_task_result_1.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/Test4DT_tests/test_pymonet_task_result_1.py:30: in <lambda>
    task = Task(lambda reject, resolve: resolve(computation()) if computation() is not None else reject(computation()))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def computation():
        if random.choice([True, False]):
            return 42
        else:
>           raise ValueError("Computation failed")
E           ValueError: Computation failed

pyMonet/Test4DT_tests/test_pymonet_task_result_1.py:28: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_result_1.py::test_random_computation
========================= 1 failed, 2 passed in 0.06s ==========================
"""