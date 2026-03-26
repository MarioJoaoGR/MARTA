
import pytest
from typing import Callable, List, Tuple

def cond(condition_list: List[Tuple[Callable[[int], bool], Callable[[int], int]]]):
    def result(*args):
        for (condition_function, execute_function) in condition_list:
            if condition_function(*args):
                return execute_function(*args)
    return result

# Test case for valid conditions
def test_valid_case():
    # Define the functions to be used as conditions and executors
    def is_even(n: int) -> bool:
        return n % 2 == 0
    
    def double(n: int) -> int:
        return n * 2
    
    def triple(n: int) -> int:
        return n * 3
    
    # Create the condition list with valid conditions and executors
    cond_func = cond([(is_even, double), (lambda x: x > 5, triple)])
    
    # Test cases for valid input
    assert cond_func(4) == 8  # is_even(4) returns True, so it uses the double function
    assert cond_func(7) == 21  # lambda x: x > 5(7) returns True, so it uses the triple function
