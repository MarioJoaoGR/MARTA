
import pytest
from pytutils.iters import dedupe_iter

def test_valid_input():
    # Test with a list of integers
    input_list = [1, 2, 3, 2, 1]
    expected_output = [1, 2, 3]
    
    result = list(dedupe_iter(input_list))
    assert result == expected_output
    
    # Test with a custom hash function
    def custom_hash(x):
        return x % 10
    
    input_list = [12, 23, 12]
    expected_output = [12, 23]
    
    result = list(dedupe_iter(input_list, hashfunc=custom_hash))
    assert result == expected_output
