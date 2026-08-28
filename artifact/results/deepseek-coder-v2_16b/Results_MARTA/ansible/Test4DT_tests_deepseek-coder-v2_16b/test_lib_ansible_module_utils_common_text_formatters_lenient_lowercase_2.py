
import pytest

def lenient_lowercase(lst):
    """Lowercase elements of a list.

    If an element is not a string, pass it through untouched.
    """
    lowered = []
    for value in lst:
        try:
            lowered.append(value.lower())
        except AttributeError:
            lowered.append(value)
    return lowered

# Test cases
def test_valid_case_all_strings():
    assert lenient_lowercase(['Hello', 'World', 'Python']) == ['hello', 'world', 'python']

def test_edge_case_empty_list():
    assert lenient_lowercase([]) == []

def test_error_case_non_string_elements():
    assert lenient_lowercase(['Hello', 123, True, 'WORLD']) == ['hello', 123, True, 'world']
