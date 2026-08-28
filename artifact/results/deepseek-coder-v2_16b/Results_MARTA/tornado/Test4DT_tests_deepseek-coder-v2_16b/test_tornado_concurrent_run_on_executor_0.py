
import pytest
from tornado.concurrent import run_on_executor
from concurrent.futures import Future
import functools

class MyClass:
    def __init__(self):
        self.executor = 'custom_executor'
    
    @run_on_executor(executor='custom_executor')
    def my_method(self, arg1=None, arg2=None):
        return f"Executing with {arg1} and {arg2}"


def test_edge_case_none_input():
    with pytest.raises(AttributeError):
        instance = MyClass()
        future = instance.my_method()

def test_invalid_inputs():
    with pytest.raises(AttributeError):
        instance = MyClass()
        future = instance.my_method(arg1="value1")