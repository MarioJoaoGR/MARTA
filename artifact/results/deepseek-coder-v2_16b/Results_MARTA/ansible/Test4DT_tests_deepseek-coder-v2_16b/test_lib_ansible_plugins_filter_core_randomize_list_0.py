
import pytest
from random import Random, shuffle
from ansible.plugins.filter.core import randomize_list


def test_valid_input_without_seed():
    original_list = [1, 2, 3, 4, 5]
    randomized_list = randomize_list(original_list)
    assert len(randomized_list) == len(original_list), "Lengths should be the same"

def test_empty_input():
    empty_list = []
    randomized_empty_list = randomize_list(empty_list)
    assert randomized_empty_list == [], "Expected an empty list but got something else"

def test_none_values():
    mixed_list = [None, 1, None, 2, None]
    randomized_mixed_list = randomize_list(mixed_list)
    assert len(randomized_mixed_list) == len(mixed_list), "Lengths should be the same"