
import pytest
from pytutils.iters import dedupe

def test_valid_input():
    @dedupe
    def some_function(iterable):
        return iterable
    
    # Test with valid input
    input_data = [1, 2, 3, 4, 5]
    result = some_function(input_data)
    assert list(result) == [1, 2, 3, 4, 5]
