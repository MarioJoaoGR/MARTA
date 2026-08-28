
import pytest
from pypara.monetary import NoneMoney

def test_none_money_abs():
    nm = NoneMoney()
    assert abs(nm) == nm

def test_none_money_add():
    money1 = NoneMoney()
    money2 = NoneMoney()
    result_add = money1 + money2
    assert isinstance(result_add, NoneMoney)

def test_none_money_sub():
    money1 = NoneMoney()
    money2 = NoneMoney()
    result_sub = money1 - money2
    assert isinstance(result_sub, NoneMoney)

def test_none_money_mul():
    money1 = NoneMoney()
    money2 = NoneMoney()
    result_mul = money1 * money2
    assert isinstance(result_mul, NoneMoney)

def test_none_money_div():
    money1 = NoneMoney()
    money2 = NoneMoney()
    result_div = money1 / money2
    assert isinstance(result_div, NoneMoney)

def test_none_money_floordiv():
    money1 = NoneMoney()
    money2 = NoneMoney()
    result_floordiv = money1 // money2
    assert isinstance(result_floordiv, NoneMoney)

def test_none_money_lt():
    money1 = NoneMoney()
    money2 = NoneMoney()
    assert (money1 < money2) == False

def test_none_money_le():
    money1 = NoneMoney()
    money2 = NoneMoney()
    assert (money1 <= money2) == True

def test_none_money_gt():
    money1 = NoneMoney()
    money2 = NoneMoney()
    assert (money1 > money2) == False

def test_none_money_ge():
    money1 = NoneMoney()
    money2 = NoneMoney()
    assert (money1 >= money2) == True
