
import pytest
from ansible.plugins.filter.core import path_join
from ansible.errors import AnsibleFilterTypeError
import os
from six import string_types
from unittest.mock import patch

def is_sequence(value):
    return isinstance(value, (list, tuple))

# Test for valid input with a single string
def test_valid_input_single_string():
    result = path_join("foo")
    assert result == "foo"

# Test for valid input with a sequence of strings
def test_valid_input_sequence_of_strings():
    result = path_join(["foo", "bar"])
    assert result == "foo/bar"

# Test for invalid input with non-string type, should raise TypeError
def test_invalid_input_non_string():
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        path_join(42)
    assert str(excinfo.value) == "|path_join expects string or sequence, got <class 'int'> instead."
