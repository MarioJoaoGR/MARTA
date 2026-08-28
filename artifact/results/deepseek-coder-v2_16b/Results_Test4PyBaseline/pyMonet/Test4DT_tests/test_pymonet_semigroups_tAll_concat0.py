# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import All

# Test creating an instance with a True value
def test_create_all_true():
    all_instance = All(True)
    assert all_instance.value is True

# Test combining two `All` instances where both values are True
def test_concat_two_true():
    all_true = All(True)
    combined = all_true.concat(All(True))
    assert combined.value is True

# Test combining two `All` instances where one value is False
def test_concat_false_and_true():
    combined_false = All(False).concat(All(True))
    assert combined_false.value is False

# Test combining two `All` instances where both values are False
def test_concat_two_false():
    combined_both_false = All(False).concat(All(False))
    assert combined_both_false.value is False

# Additional edge cases to consider:

# Combining with itself should not change the value
def test_concat_with_itself():
    all_instance = All(True)
    result = all_instance.concat(all_instance)
    assert result.value is True

# Combining with a neutral element (All(True)) should not change the value
def test_concat_with_neutral_element():
    all_false = All(False)
    result = all_false.concat(All(True))
    assert result.value is False

# Combining with an already combined instance should maintain the combined state
def test_concat_multiple_times():
    all_instance = All(True)
    combined1 = all_instance.concat(All(False))
    combined2 = combined1.concat(All(True))
    assert combined2.value is False
