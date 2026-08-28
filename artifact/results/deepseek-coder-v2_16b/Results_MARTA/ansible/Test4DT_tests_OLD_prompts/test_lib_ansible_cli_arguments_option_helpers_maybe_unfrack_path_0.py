
import pytest
from unittest.mock import patch
from ansible.cli.arguments.option_helpers import unfrackpath

def maybe_unfrack_path(beacon):
    def inner(value):
        if value.startswith(beacon):
            return beacon + unfrackpath(value[len(beacon):])
        return value
    return inner

@patch('ansible.cli.arguments.option_helpers.unfrackpath', lambda path: path.lstrip('/'))
def test_maybe_unfrack_path_basic():
    prefixed_unfrackpath = maybe_unfrack_path('prefix')
    
    # Test case 1: Input string starts with the beacon
    assert prefixed_unfrackpath("prefix/example") == "prefix/example"
    
    # Test case 2: Input string does not start with the beacon
    assert prefixed_unfrackpath("example") == "example"
    
    # Test case 3: Input string starts with a different beacon
    assert prefixed_unfrackpath("another/example") == "another/example"
