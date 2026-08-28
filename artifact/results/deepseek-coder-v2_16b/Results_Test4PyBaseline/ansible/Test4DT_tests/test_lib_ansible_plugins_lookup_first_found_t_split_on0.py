
import pytest
from ansible.plugins.lookup.first_found import _split_on

# Test case 1: Splitting a comma-separated string
def test_split_on_string():
    assert _split_on('apple,banana,orange') == ['apple', 'banana', 'orange']

# Test case 2: Splitting multiple space-separated strings within a list
def test_split_on_list():
    assert _split_on(['apple banana orange', 'grape kiwi']) == ['apple', 'banana', 'orange', 'grape', 'kiwi']

# Test case 3: Splitting a comma-separated string with custom delimiters
def test_split_on_custom_delimiters():
    assert _split_on('apple,banana,orange', spliters=' ,') == ['apple', 'banana', 'orange']

# Additional edge cases to consider:

# Test case 4: Empty string input should return an empty list
def test_split_on_empty_string():
    assert _split_on('') == []

# Test case 5: Input with only one term should return a single-element list
def test_split_on_single_term():
    assert _split_on('apple') == ['apple']

# Test case 6: Non-string input should raise a TypeError
def test_split_on_non_string_input():
    with pytest.raises(TypeError):
        _split_on(123)

# Test case 7: Input with terms separated by multiple delimiters should be split correctly
def test_split_on_multiple_delimiters():
    assert _split_on('apple;banana,orange', spliters=';,') == ['apple', 'banana', 'orange']
