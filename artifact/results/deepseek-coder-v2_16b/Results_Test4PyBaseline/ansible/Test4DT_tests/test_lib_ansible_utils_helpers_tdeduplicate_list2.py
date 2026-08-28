
import pytest
from ansible.utils.helpers import deduplicate_list

# Test case 7: Handling a list with None values (edge case)
def test_deduplicate_list_none():
    original_list = [None, 'a', None, 'b']
    expected_result = [None, 'a', 'b']
    assert deduplicate_list(original_list) == expected_result

# Test case 8: Handling a list with mixed types (edge case)
def test_deduplicate_list_mixed_types():
    original_list = ['foo', 1, 'bar', 1, None, 'foo']
    expected_result = ['foo', 1, 'bar', None]
    assert deduplicate_list(original_list) == expected_result

# Test case 9: Handling a list with large numbers (edge case)
def test_deduplicate_list_large_numbers():
    original_list = [1000000, 2000000, 1000000]
    expected_result = [1000000, 2000000]
    assert deduplicate_list(original_list) == expected_result

# Test case 10: Handling a list with negative numbers (edge case)
def test_deduplicate_list_negative_numbers():
    original_list = [-1, -2, -1, -3]
    expected_result = [-1, -2, -3]
    assert deduplicate_list(original_list) == expected_result
