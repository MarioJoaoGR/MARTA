
# Module: ansible.utils.version
import pytest
from ansible.utils.version import _Alpha

# Test cases for _Alpha class
def test__alpha_init():
    alpha = _Alpha("test")
    assert alpha.specifier == "test"

def test__alpha_comparison_with_same_instance():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    assert alpha1 == alpha2

def test__alpha_comparison_with_different_instance():
    alpha1 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert not (alpha1 == alpha3)

def test__alpha_comparison_with_string():
    alpha1 = _Alpha("test")
    assert alpha1 == "test"

def test__alpha_comparison_with_integer():
    alpha1 = _Alpha("test")
    assert not (alpha1 == 123)

def test__alpha_less_than_comparison():
    alpha1 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha1 < alpha3

def test__alpha_greater_than_comparison():
    alpha3 = _Alpha("testing")
    alpha1 = _Alpha("test")
    assert alpha3 > alpha1

def test__alpha_less_or_equal_comparison():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha1 <= alpha2 and alpha1 <= alpha3

def test__alpha_greater_or_equal_comparison():
    alpha2 = _Alpha("test")
    alpha3 = _Alpha("testing")
    assert alpha2 >= alpha2 and alpha3 >= alpha2

# Test cases for _Numeric class (assuming it has similar functionality)
def test__numeric_init_with_integer():
    num1 = _Alpha(5)
    assert num1.specifier == 5

def test__numeric_init_with_string():
    num2 = _Alpha("6")
    assert num2.specifier == 6

def test__numeric_comparison_with_integer():
    num1 = _Alpha(5)
    num2 = _Alpha("6")
    assert str(num1.specifier) < str(num2.specifier)

def test__numeric_comparison_with_string():
    num1 = _Alpha(5)
    num3 = _Alpha("7")
    assert str(num1.specifier) < str(num3.specifier)
