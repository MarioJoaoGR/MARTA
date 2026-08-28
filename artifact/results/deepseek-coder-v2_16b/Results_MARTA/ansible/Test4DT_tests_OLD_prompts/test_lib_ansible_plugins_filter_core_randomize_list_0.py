
import pytest
from ansible.plugins.filter.core import randomize_list
from unittest.mock import patch, MagicMock
import random

def test_randomize_list_without_seed():
    original_list = [1, 2, 3, 4, 5]
    with patch('random.Random') as mock_random:
        instance = mock_random.return_value
        instance.shuffle.side_effect = lambda x: x  # Mock shuffle to return the list unchanged
        
        randomized_list_first = randomize_list(original_list)
        randomized_list_second = randomize_list(original_list)
        
        assert randomized_list_first != randomized_list_second, "Lists should be different after shuffling"

def test_randomize_list_with_seed():
    original_list = [1, 2, 3, 4, 5]
    specific_seed = 42
    with patch('random.Random') as mock_random:
        instance = mock_random.return_value
        instance.shuffle.side_effect = lambda x: x  # Mock shuffle to return the list unchanged
        
        randomized_list_first = randomize_list(original_list, seed=specific_seed)
        randomized_list_second = randomize_list(original_list, seed=specific_seed)
        
        assert randomized_list_first == randomized_list_second, "Lists should be the same with a specific seed"

def test_randomize_list_empty():
    empty_list = []
    with patch('random.Random') as mock_random:
        instance = mock_random.return_value
        instance.shuffle.side_effect = lambda x: x  # Mock shuffle to return the list unchanged
        
        randomized_empty_list = randomize_list(empty_list)
        
        assert len(randomized_empty_list) == 0, "Empty list should remain empty"
