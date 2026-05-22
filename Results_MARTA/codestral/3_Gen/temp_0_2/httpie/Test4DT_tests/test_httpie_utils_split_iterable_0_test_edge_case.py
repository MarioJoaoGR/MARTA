
import pytest
from httpie.utils import split_iterable
from typing import Iterable, List, Tuple, Callable, TypeVar
from unittest.mock import patch

T = TypeVar('T')

def test_edge_case():
    with patch('httpie.utils.split_iterable', autospec=True) as mock_split:
        # Mock the split_iterable function to always return ([], []) for any input
        mock_split.return_value = ([], [])
        
        # Test edge case with an empty list
        result = split_iterable([], lambda x: True)
        
        assert result == ([], []), "Expected both lists to be empty"
