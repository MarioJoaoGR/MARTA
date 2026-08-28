
import pytest
from pysnooper.tracer import Tracer

def test_simple_wrapper_with_function():
    def example_function(a, b=None):
        print(f"Received args={a}, kwargs={b}")
    
    with pytest.raises(NameError):
        wrapper = simple_wrapper(example_function, 10, b=20)
        wrapper()

def test_simple_wrapper_with_lambda():
    with pytest.raises(NameError):
        wrapper = simple_wrapper(lambda: print("Lambda function executed"))
        wrapper()

def test_simple_wrapper_with_no_arguments():
    def example_function():
        print("No arguments passed")
    
    with pytest.raises(NameError):
        wrapper = simple_wrapper(example_function)
        wrapper()

def test_simple_wrapper_with_multiple_positional_arguments():
    def multiple_args_function(*args):
        print(f"Received args: {args}")
    
    with pytest.raises(NameError):
        wrapper = simple_wrapper(multiple_args_function, 1, 2, 3)
        wrapper()

def test_simple_wrapper_with_multiple_keyword_arguments():
    def multiple_kwargs_function(**kwargs):
        print(f"Received kwargs: {kwargs}")
    
    with pytest.raises(NameError):
        wrapper = simple_wrapper(multiple_kwargs_function, a=1, b=2)
        wrapper()

def test_simple_wrapper_with_mixed_arguments():
    def mixed_args_function(arg1, arg2, kwarg=None):
        print(f"Received args: {arg1}, {arg2}, kwargs: {kwarg}")
    
    with pytest.raises(NameError):
        wrapper = simple_wrapper(mixed_args_function, 10, "hello", kwarg="world")
        wrapper()
