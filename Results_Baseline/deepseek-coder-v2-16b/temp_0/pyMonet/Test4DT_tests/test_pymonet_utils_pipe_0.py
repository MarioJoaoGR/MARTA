
import pytest
from pymonet.utils import pipe

# Test cases for the pipe function
def test_pipe_with_single_function():
    def add_one(x):
        return x + 1
    
    result = pipe(5, add_one)
    assert result == 6

def test_pipe_with_multiple_functions():
    def add_one(x):
        return x + 1
    
    def multiply_by_two(x):
        return x * 2
    
    result = pipe(5, add_one, multiply_by_two)