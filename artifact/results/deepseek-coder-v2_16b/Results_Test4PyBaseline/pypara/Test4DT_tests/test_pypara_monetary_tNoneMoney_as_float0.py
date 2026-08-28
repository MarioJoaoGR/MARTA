
import pytest
from pypara.monetary import NoneMoney

# Test fixture for creating an instance of NoneMoney
@pytest.fixture
def undefined_money():
    return NoneMoney()

# Test case to check the __float__ method raises a TypeError when called on an undefined monetary value
def test_float_raises_type_error(undefined_money):
    with pytest.raises(TypeError) as e:
        float(undefined_money)
    assert str(e.value) == "Undefined monetary values do not have quantity information."

# Test case to check the __int__ method raises a TypeError when called on an undefined monetary value
def test_int_raises_type_error(undefined_money):
    with pytest.raises(TypeError) as e:
        int(undefined_money)
    assert str(e.value) == "Undefined monetary values do not have quantity information."

# Test case to check that two instances of NoneMoney are equal if they are both undefined
def test_equality_of_undefined_instances(undefined_money):
    another_undefined_money = NoneMoney()
    assert undefined_money == another_undefined_money

# Test case to check adding two instances of NoneMoney raises a TypeError
def test_addition_raises_type_error():
    undefined_money1 = NoneMoney()
    with pytest.raises(TypeError) as e:
        float(undefined_money1)  # This will raise an error because the method is not defined on NoneMoney class
    assert str(e.value) == "Undefined monetary values do not have quantity information."
