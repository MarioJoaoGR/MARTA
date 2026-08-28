
import pytest
from ansible.utils.version import _Alpha

def test_alpha_comparison():
    alpha1 = _Alpha("2")
    alpha2 = _Alpha("3")
    assert alpha1 < alpha2, "Expected alpha1 to be less than alpha2"

def test_alpha_string_comparison():
    alpha5 = _Alpha("10")
    assert alpha5 == "10", "Expected alpha5 to be equal to the string '10'"

def test_alpha_inequality():
    alpha3 = _Alpha("2")
    alpha4 = _Alpha("3")
    assert alpha3 != alpha4, "Expected alpha3 and alpha4 to be not equal"
