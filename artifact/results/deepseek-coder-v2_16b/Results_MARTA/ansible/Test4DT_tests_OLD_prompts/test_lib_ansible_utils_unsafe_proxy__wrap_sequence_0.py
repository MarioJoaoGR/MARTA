
import pytest
from ansible.utils.unsafe_proxy import _wrap_sequence

def test_valid_input_tuple():
    original_tuple = (1, 2, 3)
    wrapped_tuple = _wrap_sequence(original_tuple)
    assert isinstance(wrapped_tuple, tuple), "Expected a tuple"

def test_valid_input_list():
    original_list = [4, 5, 6]
    wrapped_list = _wrap_sequence(original_list)
    assert isinstance(wrapped_list, list), "Expected a list"
