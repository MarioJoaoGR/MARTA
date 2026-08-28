# Module: pypara.monetary
# test_monetary.py
from pypara.monetary import NoneMoney

def test_none_money_initialization():
    undefined_money = NoneMoney()
    assert isinstance(undefined_money, NoneMoney), "Instance should be of type NoneMoney"

def test_float_conversion():
    undefined_money = NoneMoney()
    try:
        float(undefined_money)
    except TypeError as e:
        assert str(e) == "Undefined monetary values do not have quantity information.", f"Unexpected error: {e}"

def test_int_conversion():
    undefined_money = NoneMoney()
    try:
        int(undefined_money)
    except TypeError as e:
        assert str(e) == "Undefined monetary values do not have quantity information.", f"Unexpected error: {e}"

def test_comparison():
    undefined_money1 = NoneMoney()
    undefined_money2 = NoneMoney()
    assert undefined_money1 == undefined_money2, "Instances should be equal since they are both undefined"

def test_addition():
    undefined_money1 = NoneMoney()
    undefined_money2 = NoneMoney()
    try:
        result = undefined_money1 + undefined_money2
    except TypeError as e:
        assert str(e) == "Cannot perform addition on undefined monetary values.", f"Unexpected error: {e}"

def test_subtraction():
    undefined_money1 = NoneMoney()
    undefined_money2 = NoneMoney()
    try:
        result = undefined_money1 - undefined_money2
    except TypeError as e:
        assert str(e) == "Cannot perform subtraction on undefined monetary values.", f"Unexpected error: {e}"

def test_multiplication():
    undefined_money1 = NoneMoney()
    undefined_money2 = NoneMoney()
    try:
        result = undefined_money1 * undefined_money2
    except TypeError as e:
        assert str(e) == "Cannot perform multiplication on undefined monetary values.", f"Unexpected error: {e}"

def test_division():
    undefined_money1 = NoneMoney()
    undefined_money2 = NoneMoney()
    try:
        result = undefined_money1 / undefined_money2
    except TypeError as e:
        assert str(e) == "Cannot perform division on undefined monetary values.", f"Unexpected error: {e}"

def test_floor_division():
    undefined_money1 = NoneMoney()
    undefined_money2 = NoneMoney()
    try:
        result = undefined_money1 // undefined_money2
    except TypeError as e:
        assert str(e) == "Cannot perform floor division on undefined monetary values.", f"Unexpected error: {e}"

def test_absolute_value():
    undefined_money = NoneMoney()
    assert abs(undefined_money) == undefined_money, "Absolute value of an undefined quantity should be itself"

def test_negation():
    undefined_money = NoneMoney()
    assert -undefined_money == undefined_money, "Negation of an undefined quantity should be itself"

def test_boolean_conversion():
    undefined_money = NoneMoney()
    assert bool(undefined_money) is False, "Conversion to boolean should return False for an undefined quantity"
