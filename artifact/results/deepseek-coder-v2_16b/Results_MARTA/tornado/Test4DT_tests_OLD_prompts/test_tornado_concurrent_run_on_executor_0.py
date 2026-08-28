
import pytest
from tornado.concurrent import run_on_executor, Future
import functools
import unittest.mock as mock

def test_valid_case():
    class MyClass:
        @run_on_executor(executor='custom_executor')
        def my_method(self):
            pass

    instance = MyClass()
    with pytest.raises(AttributeError):
        future = instance.my_method()

def test_edge_case():
    class MyClass:
        @run_on_executor(executor='custom_executor')
        def my_method(self):
            pass

    instance = MyClass()
    with pytest.raises(AttributeError):
        future = instance.my_method()

def test_invalid_input():
    class MyClass:
        @run_on_executor(executor='custom_executor')
        def my_method(self, arg1, arg2):
            pass

    instance = MyClass()
    with pytest.raises(AttributeError):
        future = instance.my_method('positional_arg', arg2='keyword_arg')
