
import pytest
from pymonet.semigroups import First


def test_first_instance_specific_value():
    specific_value = "initial string"
    first_instance = First(specific_value)
    assert first_instance.value == specific_value

def test_concatenation_returns_first_value():
    value1 = 42
    value2 = "hello"
    first1 = First(value1)
    first2 = First(value2)
    combined_first = first1.concat(first2)
    assert combined_first.value == value1