
import pytest
from ansible.module_utils.common.text.formatters import lenient_lowercase

# Test scenario 1: Test standard input with all string elements
def test_valid_case_all_strings():
    result = lenient_lowercase(['Hello', 'World', 'Python'])
    assert result == ['hello', 'world', 'python']

# Test scenario 2: Test edge case with an empty list
def test_edge_case_empty_list():
    result = lenient_lowercase([])
    assert result == []

# Test scenario 3: Test error handling with non-string elements
def test_error_case_non_string_elements():
    result = lenient_lowercase([1, 'a', 3.14, None])
    assert result == [1, 'a', 3.14, None]
