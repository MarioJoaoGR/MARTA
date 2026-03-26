
# Module: pymonet.utils
import pytest
from pymonet.utils import fn

# Example function to be tested
def add(a, b):
    return a + b

# Test case for currying the add function with 2 arguments
def test_curried_add():
    curried_add = fn(add, args_count=2)
    assert curried_add(1)(2) == 3

# Additional test cases to cover different scenarios
def test_curried_add_with_more_args():
    curried_add = fn(add, args_count=2)
    with pytest.raises(TypeError):
        curried_add(1)(2)(3)  # Should raise TypeError because it expects only 2 arguments

def test_curried_add_with_less_args():
    curried_add = fn(add, args_count=2)
    with pytest.raises(TypeError):
        curried_add(1)  # Should raise TypeError because it expects exactly 2 arguments

# Test case for creating a resolved task and using fork
def test_resolved_task():
    def my_fork(reject, resolve):
        resolve("example value")
    
    task = fn(my_fork)
    result = task.fork(lambda x: assert x == "example value")

# Test case for creating a rejected task and handling the error with fork
def test_rejected_task():
    def my_reject_fork(reject, resolve):
        reject("error message")
    
    task = fn(my_reject_fork)
    result = task.fork(lambda x: pytest.raises(Exception), lambda e: assert str(e) == "error message")

# Test case for using map to transform the value of a resolved task
def test_transform_resolved_task():
    def double_value(value):
        return value * 2
    
    resolved_task = fn(lambda resolve: resolve("example value"))
    transformed_task = resolved_task.map(double_value)
    result = transformed_task.fork(lambda x: assert x == "example value" * 2)

# Test case for using bind to chain another asynchronous operation
def test_chained_operation():
    def chained_operation(value):
        return fn(lambda resolve: resolve(value + 1))
    
    resolved_task = fn(lambda resolve: resolve("example value"))
    chained_task = resolved_task.bind(chained_operation)
    result = chained_task.fork(lambda x: assert x == "example value" + 1)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_fn_0
pyMonet/Test4DT_tests/test_pymonet_utils_fn_0.py:32:34: E0001: Parsing failed: 'invalid syntax (Test4DT_tests.test_pymonet_utils_fn_0, line 32)' (syntax-error)


"""