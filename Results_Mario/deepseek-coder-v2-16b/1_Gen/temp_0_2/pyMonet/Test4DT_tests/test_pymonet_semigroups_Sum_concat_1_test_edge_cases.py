
import pytest
from pymonet.semigroups import Sum

def test_concat():
    sum1 = Sum(3)
    sum2 = Sum(4)
    result = sum1.concat(sum2)
    assert result.value == 7

def test_neutral_element():
    neutral_element = Sum.neutral_element
    assert neutral_element == 0
