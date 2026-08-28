
# Module: ansible.utils.version
import pytest
from ansible.utils.version import _Alpha

# Test cases for _Alpha class
def test_alpha_init():
    alpha1 = _Alpha("test")
    assert alpha1.specifier == "test"

def test_alpha_equal():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha1 == alpha2
    assert not (alpha1 == alpha3)
    assert alpha1 == "test"
    assert not (alpha1 == 123)

def test_alpha_not_equal():
    alpha1 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha1 != alpha3
    assert alpha1 != "testing"
    assert alpha1 != 123

def test_alpha_less_than():
    alpha1 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha1 < alpha3

def test_alpha_greater_than():
    alpha1 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert not (alpha1 > alpha3)
    assert alpha3 > alpha1

def test_alpha_less_or_equal():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha1 <= alpha2
    assert alpha1 <= alpha3

def test_alpha_greater_or_equal():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha2 >= alpha1
    assert alpha3 >= alpha1

# Additional tests for __ne__ method
def test_alpha_not_equal_different_specifiers():
    alpha1 = _Alpha("test")
    alpha4 = _Alpha("tests")
    assert alpha1 != alpha4

def test_alpha_not_equal_with_string():
    alpha1 = _Alpha("test")
    assert alpha1 != "test1"

def test_alpha_not_equal_with_int():
    alpha1 = _Alpha("test")
    assert alpha1 != 123

if __name__ == "__main__":
    pytest.main()
