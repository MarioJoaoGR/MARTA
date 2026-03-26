
# Module: pymonet.lazy
import pytest
from pymonet.lazy import Lazy, Task, Left, Right

# Test initialization with a function
def test_lazy_initialization():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert not lazy.is_evaluated
    result = lazy._compute_value(5)  # Manually compute the value for testing
    assert lazy.is_evaluated
    assert result == 25

# Test mapping over a Lazy instance
def test_lazy_map():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    mapped_lazy = lazy.map(lambda x: x + 1)
    assert not lazy.is_evaluated
    result = mapped_lazy._compute_value(5)  # Manually compute the value for testing
    assert lazy.is_evaluated
    assert result == 26

# Test creating a Lazy instance with a constant value
def test_lazy_of():
    lazy_constant = Lazy.of(42)
    assert not lazy_constant.is_evaluated
    result = lazy_constant._compute_value()  # Manually compute the value for testing
    assert lazy_constant.is_evaluated
    assert result == 42

# Test folding a Lazy instance
def test_lazy_fold():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    result = lazy.fold()
    assert lazy.is_evaluated
    assert result == 25

# Test mapping over a Task instance
def test_task_map():
    def my_fork(reject, resolve):
        resolve(42)
    
    task = Task(my_fork)
    mapped_task = task.map(lambda x: x * 2)
    result = mapped_task.fork(lambda x: f"Rejected: {x}", lambda x: f"Resolved: {x}")
    assert result == "Resolved: 84"

# Test chaining tasks with bind
def test_task_bind():
    def my_fork(reject, resolve):
        resolve(21)
    
    task = Task(my_fork)
    chained_task = task.bind(lambda x: Task.of(x + 5))
    result = chained_task.fork(lambda x: f"Rejected: {x}", lambda x: f"Resolved: {x}")
    assert result == "Resolved: 26"

# Test mapping over an Either instance
def test_either_map():
    either_instance = Left("error message")
    mapped_either = either_instance.map(lambda x: f"Error: {x}")
    assert mapped_either.value == "Error: error message"

# Test binding over an Either instance
def test_either_bind():
    either_instance = Left("error message")
    result = either_instance.bind(lambda x: Right(x + " bound"))
    assert isinstance(result, Left)
    assert result.value == "error message"

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy__compute_value_0
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy__compute_value_0.py:4:0: E0611: No name 'Task' in module 'pymonet.lazy' (no-name-in-module)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy__compute_value_0.py:4:0: E0611: No name 'Left' in module 'pymonet.lazy' (no-name-in-module)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy__compute_value_0.py:4:0: E0611: No name 'Right' in module 'pymonet.lazy' (no-name-in-module)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy__compute_value_0.py:43:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""