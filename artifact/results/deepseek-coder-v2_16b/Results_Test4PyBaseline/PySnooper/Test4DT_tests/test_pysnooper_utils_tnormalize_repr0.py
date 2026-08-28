# Module: pysnooper.utils
# test_pysnooper_utils.py
from pysnooper.utils import normalize_repr, DEFAULT_REPR_RE
import re

def test_normalize_repr_with_memory_address():
    obj_repr = '<__main__.SomeClass object at 0x123456789>'
    expected_output = '<__main__.SomeClass object>'
    assert normalize_repr(obj_repr) == expected_output, f"Expected '{expected_output}', but got '{normalize_repr(obj_repr)}'"

def test_normalize_repr_without_memory_address():
    another_obj_repr = 'This is a string'
    assert normalize_repr(another_obj_repr) == another_obj_repr, f"Expected '{another_obj_repr}', but got '{normalize_repr(another_obj_repr)}'"

def test_normalize_repr_with_invalid_input():
    invalid_input = 12345  # Invalid input type to ensure function handles non-string inputs gracefully
    try:
        normalize_repr(invalid_input)
    except TypeError as e:
        assert True, f"Expected a TypeError for invalid input, but got {e}"
    else:
        assert False, "Expected a TypeError for invalid input, but no error was raised."

def test_default_repr_re():
    # Ensure DEFAULT_REPR_RE is defined and is a compiled regular expression
    assert isinstance(DEFAULT_REPR_RE, re.Pattern), f"DEFAULT_REPR_RE should be a compiled regular expression, but got {type(DEFAULT_REPR_RE)}"
    assert hasattr(DEFAULT_REPR_RE, 'pattern'), "DEFAULT_REPR_RE should have a pattern attribute"
