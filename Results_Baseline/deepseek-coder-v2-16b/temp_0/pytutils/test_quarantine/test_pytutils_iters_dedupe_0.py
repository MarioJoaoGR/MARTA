
# Module: pytutils.iters
import pytest
from pytutils.iters import dedupe

# Example function to be decorated
def my_func():
    return [1, 2, 3, 2, 1]

@dedupe(my_func, instance=None, args=(), kwargs={})
def my_func():
    return [1, 2, 3, 2, 1]

# Test cases for dedupe function
def test_dedupe_function():
    # Test with a function that returns an iterable
    @dedupe(my_func, instance=None, args=(), kwargs={})
    def my_func():
        return [1, 2, 3, 2, 1]
    
    assert list(my_func()) == [1, 2, 3]

def test_dedupe_method():
    # Test with a method of a class instance
    class MyClass:
        def my_method(self):
            return [1, 2, 3, 2, 1]
    
    instance = MyClass()
    @dedupe(instance.my_method, instance=instance, args=(), kwargs={})
    def my_method():
        return [1, 2, 3, 2, 1]
    
    assert list(my_method()) == [1, 2, 3]

def test_dedupe_static_method():
    # Test with a static method of a class
    class MyClass:
        @staticmethod
        def my_static_method():
            return [1, 2, 3, 2, 1]
    
    @dedupe(MyClass.my_static_method, instance=None, args=(), kwargs={})
    def my_static_method():
        return [1, 2, 3, 2, 1]
    
    assert list(my_static_method()) == [1, 2, 3]

def test_dedupe_class_method():
    # Test with a class method
    class MyClass:
        @classmethod
        def my_class_method(cls):
            return [1, 2, 3, 2, 1]
    
    @dedupe(MyClass.my_class_method, instance=None, args=(), kwargs={})
    def my_class_method():
        return [1, 2, 3, 2, 1]
    
    assert list(my_class_method()) == [1, 2, 3]

def test_dedupe_function_with_args_and_kwargs():
    # Test with a function that takes arguments and keyword arguments
    def my_func_with_args_and_kwargs(a, b=None):
        return [a, b, a]
    
    @dedupe(my_func_with_args_and_kwargs, instance=None, args=(1,), kwargs={'b': 2})
    def my_func_with_args_and_kwargs(a, b=None):
        return [a, b, a]
    
    assert list(my_func_with_args_and_kwargs()) == [1, 2, 1]

# Run the tests
if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_iters_dedupe_0
pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0.py:11:0: E0102: function already defined line 7 (function-redefined)
pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0.py:68:4: E0102: function already defined line 64 (function-redefined)
pytutils/Test4DT_tests/test_pytutils_iters_dedupe_0.py:71:16: E1120: No value for argument 'a' in function call (no-value-for-parameter)


"""