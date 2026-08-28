
import pytest
from pymonet.semigroups import All

# Scenario 1: Test concatenation of two All instances with both values being True
def test_valid_concat_true_true():
    all_true = All(True)
    all_true2 = All(True)
    combined_all = all_true.concat(all_true2)
    assert combined_all.value is True

# Scenario 2: Test concatenation of an All instance with value True and another with value False
def test_valid_concat_true_false():
    all_true = All(True)
    all_false = All(False)
    combined_all = all_true.concat(all_false)
    assert combined_all.value is False

# Scenario 3: Test concatenation of two All instances with both values being False
def test_valid_concat_false_false():
    all_false1 = All(False)
    all_false2 = All(False)
    combined_all = all_false1.concat(all_false2)
    assert combined_all.value is False
