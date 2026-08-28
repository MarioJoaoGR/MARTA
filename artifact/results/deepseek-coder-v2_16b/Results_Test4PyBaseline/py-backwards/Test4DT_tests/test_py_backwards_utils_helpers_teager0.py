
# Module: py_backwards.utils.helpers
# Import the function correctly using its module name.
from py_backwards.utils.helpers import eager
from typing import Callable, Iterable, List, TypeVar, Any
from functools import wraps

T = TypeVar('T')

def test_eager_with_generator():
    def generate_numbers():
        for i in range(10):
            yield i
    
    eager_generate_numbers = eager(generate_numbers)
    assert list(eager_generate_numbers()) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_eager_with_squares():
    def generate_squares():
        for i in range(10):
            yield i ** 2
    
    eager_generate_squares = eager(generate_squares)
    assert list(eager_generate_squares()) == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def test_eager_with_empty_generator():
    def generate_empty():
        pass
    
    eager_generate_empty = eager(generate_empty)