
# Module: ansible.utils.lock
# test_lock_decorator.py
from ansible.utils.lock import lock_decorator
import threading
from functools import wraps

# Test the decorator with a predefined attribute
def test_lock_decorator_with_attribute():
    def mock_function(arg1, arg2=None):
        return (arg1, arg2)

    @lock_decorator(attr='_callback_lock')
    def wrapped_mock_function(arg1, arg2=None):
        return (arg1, arg2)

    # Create a mock object with the attribute
    class MockObject:
        _callback_lock = threading.Lock()

    # Test without arguments
    result = wrapped_mock_function(MockObject(), 1)
    assert result == (1, None), f"Expected (1, None), but got {result}"

    # Test with arguments
    result = wrapped_mock_function(MockObject(), arg2=2)
    assert result == (1, 2), f"Expected (1, 2), but got {result}"

# Test the decorator with an explicit lock
def test_lock_decorator_with_explicit_lock():
    def mock_function(arg1, arg2=None):
        return (arg1, arg2)

    @lock_decorator(lock=threading.Lock())
    def wrapped_mock_function(arg1, arg2=None):
        return (arg1, arg2)

    # Create a mock object with the attribute
    class MockObject:
        pass

    lock = threading.Lock()
    setattr(MockObject, '_lock', lock)

    # Test without arguments
    result = wrapped_mock_function(MockObject(), 1)
    assert result == (1, None), f"Expected (1, None), but got {result}"

    # Test with arguments
    result = wrapped_mock_function(MockObject(), arg2=2)
    assert result == (1, 2), f"Expected (1, 2), but got {result}"

# Test the decorator without any lock specified
def test_lock_decorator_without_lock():
    def mock_function(arg1, arg2=None):
        return (arg1, arg2)

    @lock_decorator()
    def wrapped_mock_function(arg1, arg2=None):
        return (arg1, arg2)

    # Create a mock object with the attribute
    class MockObject:
        pass

    lock = threading.Lock()
    setattr(MockObject, 'missing_lock_attr', lock)

    # Test without arguments
    result = wrapped_mock_function(MockObject(), 1)
    assert result == (1, None), f"Expected (1, None), but got {result}"

    # Test with arguments
    result = wrapped_mock_function(MockObject(), arg2=2)
    assert result == (1, 2), f"Expected (1, 2), but got {result}"
