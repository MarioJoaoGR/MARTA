
import pytest
from typing import Callable, List, Tuple

# Assuming this is your implementation of cond function
def cond(condition_list: List[Tuple[Callable[[int], bool], Callable[[int], int]]]):
    def result(*args):
        for (condition_function, execute_function) in condition_list:
            if condition_function(*args):
                return execute_function(*args)
    return result

# Test cases for cond function
@pytest.mark.parametrize("condition_list, input_value, expected", [
    ([(lambda n: n % 2 == 0, lambda n: n * 2)], 4, 8),
    ([(lambda n: n > 5, lambda n: n * 3)], 7, 21),
    ([(lambda n: n < 0, lambda n: -n), (lambda n: n >= 0, lambda n: n)], -1, 1),
    ([], 5, None)  # No conditions met, should return None or raise an error depending on implementation
])
def test_valid_case(condition_list, input_value, expected):
    assert cond(condition_list)(input_value) == expected
