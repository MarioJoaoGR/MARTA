
import pytest
from ansible.plugins.filter.core import path_join
from ansible.errors import AnsibleFilterTypeError
import os
from six import string_types, text_type

def is_sequence(obj):
    return hasattr(obj, '__getitem__') and not isinstance(obj, (str, bytes))

# Test scenarios

def test_valid_input_single_string():
    result = path_join("foo")
    assert result == "foo"

def test_valid_input_sequence_of_strings():
    result = path_join(["foo", "bar"])
    assert result == "foo/bar" if os.name == 'nt' else "foo/bar"  # Adjust for different OS separators

def test_invalid_input_non_string_or_sequence():
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        path_join(42)
    assert str(excinfo.value) == "|path_join expects string or sequence, got <class 'int'> instead."
