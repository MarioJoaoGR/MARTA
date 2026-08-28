
import pytest
from ansible.module_utils.common.collections import is_sequence

# Test Scenario 1: Check if a list is recognized as a sequence
def test_is_sequence_list():
    assert is_sequence([1, 2, 3]) == True

# Test Scenario 2: Check if a tuple is recognized as a sequence
def test_is_sequence_tuple():
    assert is_sequence((1, 2, 3)) == True

# Test Scenario 3: Check if a set is recognized as a sequence

# Test Scenario 4: Check if a string is not recognized as a sequence by default
def test_is_sequence_string_default():
    assert is_sequence("Hello") == False

# Test Scenario 5: Check if including strings as sequences allows strings to be recognized
def test_is_sequence_string_include():
    assert is_sequence("Hello", include_strings=True) == True

# Test Scenario 6: Check if bytes are not recognized as a sequence by default
def test_is_sequence_bytes_default():
    assert is_sequence(b"Hello") == False

# Test Scenario 7: Check if including strings as sequences allows bytes to be recognized
def test_is_sequence_bytes_include():
    assert is_sequence(b"Hello", include_strings=True) == True

# Test Scenario 8: Check if a non-indexable object is not recognized as a sequence
def test_is_sequence_non_indexable():
    assert is_sequence(42) == False