# Module: pypara.monetary
# Import the function from the module
from pypara.monetary import NoneMoney

import pytest

# Test cases for the is_equal method of NoneMoney class
def test_is_equal_same_instance():
    none_money = NoneMoney()
    another_none_money = NoneMoney()
    assert none_money.is_equal(another_none_money) == True, "Expected True because both are instances of the same class"

def test_is_equal_different_class():
    none_money = NoneMoney()
    some_other_object = object()
    assert none_money.is_equal(some_other_object) == False, "Expected False because they are different classes"

# Additional edge cases can be added to cover more scenarios if needed
