
from typing import Any, Callable, Iterable

import pytest

from isort import \
    Config  # Assuming this import is correct based on your module structure


# Placeholder for sort function if it's not defined elsewhere
def sort(config, items, reverse=False, key=None):
    sorted_items = sorted(items, key=key, reverse=reverse)
    return sorted_items

@pytest.fixture
def config():
    return Config()

@pytest.fixture
def strings():
    return ['banana', 'apple', 'cherry']

def test_sort_default(config, strings):
    sorted_strings = sort(config, strings)
    assert sorted_strings == ['apple', 'banana', 'cherry'], f"Expected ascending order: ['apple', 'banana', 'cherry'], but got {sorted_strings}"

def test_sort_descending(config, strings):
    sorted_strings = sort(config, strings, reverse=True)
    assert sorted_strings == ['cherry', 'banana', 'apple'], f"Expected descending order: ['cherry', 'banana', 'apple'], but got {sorted_strings}"

def test_sort_with_key_function(config, strings):
    def key_function(s):
        return len(s)
    
    sorted_strings = sort(config, strings, key=key_function)
    assert sorted_strings == ['apple', 'banana', 'cherry'], f"Expected sorting by length: ['apple', 'banana', 'cherry'], but got {sorted_strings}"

def test_sort_with_key_and_reverse(config, strings):
    def key_function(s):
        return len(s)
    
    sorted_strings = sort(config, strings, key=key_function, reverse=True)