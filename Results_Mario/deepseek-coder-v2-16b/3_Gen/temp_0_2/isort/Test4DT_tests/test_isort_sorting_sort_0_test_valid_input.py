
import pytest
from unittest.mock import MagicMock
from isort.sorting import sort

def test_valid_input():
    # Create a mock Config object with a stubbed sorting_function method
    config = MagicMock()
    config.sorting_function = lambda to_sort, key=None, reverse=False: sorted(to_sort, key=key, reverse=reverse)
    
    # Test case for valid input
    result = sort(config, ['apple', 'banana', 'cherry'])
    assert result == ['apple', 'banana', 'cherry']  # Default sorting should be ascending without a key

    # Test case with custom key
    custom_key = lambda x: len(x)
    result_with_key = sort(config, ['apple', 'banana', 'cherry'], key=custom_key)
    assert result_with_key == sorted(['apple', 'banana', 'cherry'], key=custom_key)

    # Test case with reverse flag set to True
    result_reverse = sort(config, ['apple', 'banana', 'cherry'], reverse=True)
    assert result_reverse == sorted(['apple', 'banana', 'cherry'], reverse=True)
