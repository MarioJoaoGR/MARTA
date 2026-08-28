
import pytest
from random import Random, shuffle
from ansible.plugins.filter.core import randomize_list


def test_valid_input_without_seed():
    original_list = [1, 2, 3, 4, 5]
    randomized_list = randomize_list(original_list)
    assert len(randomized_list) == len(original_list), "Expected the same length list without a seed"

def test_empty_list():
    empty_list = []
    randomized_empty_list = randomize_list(empty_list)
    assert len(randomized_empty_list) == 0, "Expected an empty list for an empty input"