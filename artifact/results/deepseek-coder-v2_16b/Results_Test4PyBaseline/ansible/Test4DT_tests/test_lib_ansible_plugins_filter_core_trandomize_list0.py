
import pytest
from random import Random, shuffle
from ansible.plugins.filter.core import randomize_list

# Test cases for randomize_list function

def test_randomize_list_without_seed():
    original_list = [1, 2, 3, 4, 5]
    randomized_list = randomize_list(original_list)
    assert len(randomized_list) == len(original_list), "The length of the list should remain the same"
    assert set(randomized_list) == set(original_list), "The elements in the list should be the same"
    assert randomized_list != original_list, "The order of the elements should have changed"

def test_randomize_list_with_specific_seed():
    original_list = [1, 2, 3, 4, 5]
    specific_seed = 12345
    deterministic_list = randomize_list(original_list, seed=specific_seed)
    assert len(deterministic_list) == len(original_list), "The length of the list should remain the same"
    assert set(deterministic_list) == set(original_list), "The elements in the list should be the same"
    assert deterministic_list != original_list, "The order of the elements should have changed due to the seed"

def test_randomize_list_with_empty_list():
    empty_list = []
    randomized_empty_list = randomize_list(empty_list)
    assert randomized_empty_list == [], "An empty list remains an empty list after shuffling"

def test_randomize_list_with_non_list_parameter():
    invalid_input = "not a list"
    with pytest.raises(TypeError):  # Corrected the expected exception type to TypeError
        randomize_list(invalid_input)

def test_randomize_list_with_large_dataset():
    large_list = list(range(10000))  # Create a large list of integers
    randomized_large_list = randomize_list(large_list)
    assert len(randomized_large_list) == len(large_list), "The length of the list should remain the same"
    assert set(randomized_large_list) == set(large_list), "The elements in the list should be the same"
    assert randomized_large_list != large_list, "The order of the elements should have changed for a large dataset"
