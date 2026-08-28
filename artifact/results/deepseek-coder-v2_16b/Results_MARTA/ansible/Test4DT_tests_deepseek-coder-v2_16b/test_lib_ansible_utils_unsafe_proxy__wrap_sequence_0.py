
import pytest
from ansible.utils.unsafe_proxy import wrap_var

def _wrap_sequence(v):
    """Wraps a sequence with unsafe, not meant for strings, primarily tuple and list."""
    v_type = type(v)
    return v_type(wrap_var(item) for item in v)

# Test scenarios

@pytest.fixture
def original_tuple():
    return (1, 2, 3)

@pytest.fixture
def original_list():
    return [4, 5, 6]

@pytest.fixture
def invalid_input():
    return 123

# Test valid input with a tuple
def test_valid_input_tuple(original_tuple):
    wrapped_tuple = _wrap_sequence(original_tuple)
    assert isinstance(wrapped_tuple, tuple), "Expected a tuple"
    assert len(wrapped_tuple) == 3, "Expected length of 3"
    for item in wrapped_tuple:
        assert isinstance(item, type(1)), "Each item should be of the same type as the original elements"

# Test valid input with a list
def test_valid_input_list(original_list):
    wrapped_list = _wrap_sequence(original_list)
    assert isinstance(wrapped_list, list), "Expected a list"
    assert len(wrapped_list) == 3, "Expected length of 3"
    for item in wrapped_list:
        assert isinstance(item, type([1])[0]), "Each item should be of the same type as the original elements"

# Test invalid input type
def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        _wrap_sequence(invalid_input)
