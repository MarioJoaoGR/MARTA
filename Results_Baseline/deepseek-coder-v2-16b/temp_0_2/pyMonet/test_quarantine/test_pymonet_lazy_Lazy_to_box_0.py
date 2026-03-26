
# Module: pymonet.lazy
import pytest
from pymonet.lazy import Lazy, Try, Task, Left, Right

# Test initialization with a function
def test_lazy_initialization():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert not lazy.is_evaluated
    assert lazy.constructor_fn == square
    
    result = lazy.fold()  # Now the function is evaluated and stored in 'value'
    assert lazy.is_evaluated
    assert lazy.value == 25
    assert result == 25

# Test transforming with map
def test_lazy_map():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    mapped_lazy = lazy.map(lambda x: x + 1)  # Map function to add 1 to the result of the constructor function
    
    assert not lazy.is_evaluated
    assert not mapped_lazy.is_evaluated
    
    result = mapped_lazy.fold()  # Output will be (5*5)+1 = 26
    assert mapped_lazy.is_evaluated
    assert mapped_lazy.value == 26
    assert result == 26

# Test using of class method
def test_lazy_of():
    lazy_instance = Lazy.of(lambda: 42)
    assert not lazy_instance.is_evaluated
    
    result = lazy_instance.fold()
    assert lazy_instance.is_evaluated
    assert lazy_instance.value == 42
    assert result == 42

# Test handling errors with Try
def test_lazy_try():
    try_success = Try(42, True)
    try_failure = Try("error", False)
    
    def divide_by_two(x):
        if x % 2 == 0:
            return x / 2
        else:
            raise ValueError("Number is not even")
    
    try_even = try_success.map(divide_by_two)
    assert not try_even.is_evaluated
    
    result_even = try_even.get()
    assert try_even.is_evaluated
    assert result_even == 21.0
    
    try_odd_mapped = try_failure.map(divide_by_two)
    assert not try_odd_mapped.is_evaluated
    
    error_message = try_odd_mapped.on_fail(lambda e: str(e))
    assert try_odd_mapped.is_evaluated
    assert error_message == "Error: Number is not even"

# Test using Task for asynchronous operations
def test_lazy_task():
    def async_task():
        import time
        time.sleep(1)
        return "done"
    
    task = Task(lambda reject, resolve: resolve(async_task()))
    assert not task.is_evaluated
    
    result_task = task.fork(lambda e: f"Error: {e}", lambda r: r)
    assert task.is_evaluated
    assert result_task == "done"

# Test handling potential errors with Either
def test_lazy_either():
    left_value = Left("error message")
    mapped_left = left_value.map(lambda x: f"Error: {x}")
    assert not mapped_left.is_evaluated
    
    error_message = mapped_left.on_fail(lambda e: str(e))
    assert mapped_left.is_evaluated
    assert error_message == "Error: error message"
    
    right_value = Right(42)
    mapped_right = right_value.map(lambda x: x * 2)
    assert not mapped_right.is_evaluated
    
    result_right = mapped_right.get()
    assert mapped_right.is_evaluated
    assert result_right == 84

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_to_box_0
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_box_0.py:4:0: E0611: No name 'Try' in module 'pymonet.lazy' (no-name-in-module)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_box_0.py:4:0: E0611: No name 'Task' in module 'pymonet.lazy' (no-name-in-module)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_box_0.py:4:0: E0611: No name 'Left' in module 'pymonet.lazy' (no-name-in-module)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_box_0.py:4:0: E0611: No name 'Right' in module 'pymonet.lazy' (no-name-in-module)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_box_0.py:15:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_box_0.py:31:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_box_0.py:41:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""