
import pytest
from ansible.plugins.lookup.first_found import _split_on

# Test for valid input string
def test_valid_input_string():
    terms = 'apple,banana,orange'
    expected_output = ['apple', 'banana', 'orange']
    assert _split_on(terms) == expected_output

# Test for valid input list
def test_valid_input_list():
    terms = ['apple banana', 'orange']
    expected_output = ['apple', 'banana', 'orange']
    assert _split_on(terms) == expected_output

# Test for invalid input (None)
def test_invalid_input_none():
    terms = None
    with pytest.raises(TypeError):
        _split_on(terms)
