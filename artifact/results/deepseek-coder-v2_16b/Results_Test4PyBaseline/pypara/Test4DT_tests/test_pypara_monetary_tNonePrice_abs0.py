
import pytest
from pypara.monetary import NonePrice

# Test cases for NonePrice class methods

def test_abs():
    price = NonePrice()
    assert id(price.abs()) == id(price)

@pytest.mark.xfail(reason="Undefined monetary values do not have a float representation.")
def test_float():
    price = NonePrice()
    with pytest.raises(TypeError):
        float(price)

@pytest.mark.xfail(reason="Undefined monetary values do not have a int representation.")
def test_int():
    price = NonePrice()
    with pytest.raises(TypeError):
        int(price)

@pytest.mark.xfail(reason="Negation is not meaningful for undefined prices.")
def test_neg():
    price = NonePrice()
    with pytest.raises(TypeError):
        neg_price = -price

@pytest.mark.xfail(reason="Positivity is not meaningful for undefined prices.")
def test_pos():
    price = NonePrice()
    with pytest.raises(TypeError):
        pos_price = +price

@pytest.mark.xfail(reason="Addition of undefined prices does not make sense.")
def test_add():
    price1 = NonePrice()
    price2 = NonePrice()
    assert id(price1 + price2) == id(price1)

@pytest.mark.xfail(reason="Subtraction of undefined prices does not make sense.")
def test_sub():
    price1 = NonePrice()
    price2 = NonePrice()
    assert id(price1 - price2) == id(price1)

@pytest.mark.xfail(reason="Multiplication with a scalar is not meaningful for undefined prices.")
def test_mul():
    price = NonePrice()
    scalar = 2
    with pytest.raises(TypeError):
        result_multiply = price * scalar

@pytest.mark.xfail(reason="True division with a scalar is not meaningful for undefined prices.")
def test_truediv():
    price = NonePrice()
    scalar = 2
    with pytest.raises(TypeError):
        result_divide = price / scalar

@pytest.mark.xfail(reason="Floor division with a scalar is not meaningful for undefined prices.")
def test_floordiv():
    price = NonePrice()
    scalar = 2
    with pytest.raises(TypeError):
        result_floor_divide = price // scalar

@pytest.mark.xfail(reason="Comparison operators are not meaningful for undefined prices.")
def test_lt():
    price1 = NonePrice()
    price2 = NonePrice()
    assert not (price1 < price2)

@pytest.mark.xfail(reason="Comparison operators are not meaningful for undefined prices.")
def test_lte():
    price1 = NonePrice()
    price2 = NonePrice()
    assert price1 <= price2

@pytest.mark.xfail(reason="Comparison operators are not meaningful for undefined prices.")
def test_gt():
    price1 = NonePrice()
    price2 = NonePrice()
    assert not (price1 > price2)

@pytest.mark.xfail(reason="Comparison operators are not meaningful for undefined prices.")
def test_gte():
    price1 = NonePrice()
    price2 = NonePrice()
    assert price1 >= price2
