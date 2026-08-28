
# Module: ansible.plugins.filter.core
import pytest
from ansible.plugins.filter import core
import os
from typing import List, Union

# Mocking the necessary functions and types for testing
def is_sequence(obj):
    return isinstance(obj, (list, tuple))

string_types = str
AnsibleFilterTypeError = TypeError

# Test cases for path_join function
@pytest.mark.parametrize("paths, expected", [
    ("foo", 'foo'),  # Single path component as string
    (["foo", "bar"], 'foo/bar'),  # Multiple path components in a list
    (["foo/", "bar/"], 'foo/bar/'),  # Paths with trailing slashes
    (["foo", "/bar"], '/bar'),  # Combining paths with absolute paths
])
def test_path_join(paths, expected):
    if isinstance(paths, str):
        assert core.path_join(paths) == expected
    elif is_sequence(paths):
        assert core.path_join(paths) == expected
    else:
        with pytest.raises(AnsibleFilterTypeError):
            core.path_join(paths)

# Additional test cases for uncovered lines 561-564 and 566
@pytest.mark.parametrize("paths", [
    123,       # Invalid type: int
    [],        # Valid sequence but empty
    {},        # Invalid type: dict
    (1, 2),    # Valid sequence but contains an int
])
def test_path_join_with_invalid_input(paths):
    with pytest.raises(AnsibleFilterTypeError):
        core.path_join(paths)

@pytest.mark.parametrize("paths", [
    ["foo", "bar"],  # Valid sequence of strings
    ["foo/", "bar/"], # Valid sequence with trailing slashes
])
def test_path_join_with_valid_sequence(paths):
    assert core.path_join(paths) == os.path.join(*paths)
