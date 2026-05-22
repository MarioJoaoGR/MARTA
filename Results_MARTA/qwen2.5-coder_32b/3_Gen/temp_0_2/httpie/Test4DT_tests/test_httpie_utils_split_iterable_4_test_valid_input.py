
import pytest
from httpie.utils import split_iterable
from typing import Iterable, List, Tuple, Callable, TypeVar
from unittest.mock import patch

T = TypeVar('T')

def test_valid_input():
    with patch('httpie.utils.split_iterable', autospec=True) as mock_split:
        # Mock the behavior of split_iterable to return a known result for testing
        def key_function(x):
            return x % 2 == 0
        
        mock_split.return_value = ([2, 4], [1, 3, 5])
        
        # Call the function with valid input
        result = split_iterable([1, 2, 3, 4, 5], key_function)
        
        # Assert that the mock was called correctly
        assert result == ([2, 4], [1, 3, 5])
