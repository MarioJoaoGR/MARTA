
import pytest
from pymonet.semigroups import Sum

def test_sum_concat():
    s1 = Sum(3)
    s2 = Sum(4)
    result = s1.concat(s2)
    assert result.value == 7

def test_sum_neutral_element():
    neutral_sum = Sum(0)
    other_sum = Sum(5)
    combined_sum = neutral_sum.concat(other_sum)
    assert combined_sum.value == 5

def test_sum_self_concat():
    s1 = Sum(3)
    result = s1.concat(s1)
    assert result.value == 6
