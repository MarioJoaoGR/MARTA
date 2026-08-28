# Module: ansible.utils.helpers
import pytest
from ansible.utils.helpers import deduplicate_list

# Test case 1: Removing duplicates from a list of integers
def test_deduplicate_list_integers():
    original_list = [1, 2, 3, 2, 4, 1]
    expected_result = [1, 2, 3, 4]
    assert deduplicate_list(original_list) == expected_result

# Test case 2: Removing duplicates from a list of strings
def test_deduplicate_list_strings():
    original_list = ['apple', 'banana', 'cherry', 'banana']
    expected_result = ['apple', 'banana', 'cherry']
    assert deduplicate_list(original_list) == expected_result

# Test case 3: Handling an empty list
def test_deduplicate_list_empty():
    original_list = []
    expected_result = []
    assert deduplicate_list(original_list) == expected_result

# Test case 4: Handling a list with all identical elements
def test_deduplicate_list_identical():
    original_list = [7, 7, 7, 7]
    expected_result = [7]
    assert deduplicate_list(original_list) == expected_result

# Test case 5: List with all unique elements
def test_deduplicate_list_unique():
    original_list = [10, 20, 30, 40]
    expected_result = [10, 20, 30, 40]
    assert deduplicate_list(original_list) == expected_result

# Test case 6: List with some duplicate elements
def test_deduplicate_list_some_duplicates():
    original_list = [1, 2, 2, 3, 4, 4, 5]
    expected_result = [1, 2, 3, 4, 5]
    assert deduplicate_list(original_list) == expected_result
