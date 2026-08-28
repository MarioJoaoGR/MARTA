
# Module: ansible.utils.version
import pytest
from ansible.utils.version import _Alpha

# Test cases for __eq__ method of _Alpha class
def test_alpha_equal():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    assert alpha1 == alpha2  # True, because both hold the same string "test"

def test_alpha_not_equal():
    alpha1 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert not (alpha1 == alpha3)  # False, because "test" is not equal to "testing"

def test_alpha_string_equal():
    alpha1 = _Alpha("test")
    assert alpha1 == "test"  # True, because the instance holds the string "test"

def test_alpha_integer_not_equal():
    alpha1 = _Alpha("test")
    assert not (alpha1 == 123)  # False, because an integer cannot be compared directly with a string or another instance of `_Alpha`

# Additional test cases for __eq__ method to cover uncovered lines
def test_alpha_equal_different_instances():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    assert alpha1 == alpha2  # True, because both hold the same string "test"

def test_alpha_not_equal_different_types():
    alpha1 = _Alpha("test")
    assert not (alpha1 == 123)  # False, because an integer cannot be compared directly with a string or another instance of `_Alpha`

def test_alpha_not_equal_string_vs_instance():
    alpha1 = _Alpha("test")
    assert not (alpha1 == "testing")  # False, because the string "test" is not equal to the string "testing"

def test_alpha_equal_self():
    alpha1 = _Alpha("test")
    assert alpha1 == alpha1  # True, because an instance is always equal to itself

# Test cases for __ne__ method of _Alpha class
def test_alpha_not_equal_method():
    alpha1 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha1 != alpha3  # True, because "test" is not equal to "testing"

# Test cases for comparison operators (<, >, <=, >=) with _Alpha class
def test_alpha_less_than():
    alpha1 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha1 < alpha3  # True, because 'test' is less than 'testing' when treated as strings

def test_alpha_greater_than():
    alpha3 = _Alpha("testing")
    alpha1 = _Alpha("test")
    assert alpha3 > alpha1  # True, because 'testing' is greater than 'test' when treated as strings

def test_alpha_less_or_equal():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha1 <= alpha2  # True, because both are "test"
    assert alpha1 <= alpha3  # True, because "test" is less than or equal to "testing"

def test_alpha_greater_or_equal():
    alpha2 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha2 >= alpha2  # True, because both are "test"
    assert alpha3 >= alpha2  # True, because "testing" is greater than or equal to "test"

# Test cases for __init__ method of _Alpha class
def test_alpha_init():
    alpha = _Alpha("test")
    assert alpha.specifier == "test"  # Check if the specifier is correctly assigned
