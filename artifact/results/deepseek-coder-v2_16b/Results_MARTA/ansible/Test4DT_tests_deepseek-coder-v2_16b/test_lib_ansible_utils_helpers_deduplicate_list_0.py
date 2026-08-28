
import pytest

def deduplicate_list(original_list):
    """
    Creates a deduplicated list with the order in which each item is first found.
    """
    seen = set()
    return [x for x in original_list if x not in seen and not seen.add(x)]

# Test cases
def test_valid_input():
    original_list = [1, 2, 3, 2, 4, 1]
    expected_output = [1, 2, 3, 4]
    assert deduplicate_list(original_list) == expected_output

def test_empty_list():
    original_list = []
    expected_output = []
    assert deduplicate_list(original_list) == expected_output

def test_invalid_input():
    with pytest.raises(TypeError):
        deduplicate_list([[1], [2]])
