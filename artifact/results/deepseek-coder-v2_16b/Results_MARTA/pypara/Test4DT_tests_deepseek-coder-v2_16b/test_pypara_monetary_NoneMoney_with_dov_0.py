
from pypara.monetary import NoneMoney
import pytest
from datetime import date

def test_none_money_bool():
    none_money = NoneMoney()
    assert bool(none_money) == False, "Expected bool value of NoneMoney to be False"

def test_none_money_to_float():
    none_money = NoneMoney()
    with pytest.raises(TypeError):
        float(none_money), "Expected TypeError when converting NoneMoney to float"

def test_none_money_to_int():
    none_money = NoneMoney()
    with pytest.raises(TypeError):
        int(none_money), "Expected TypeError when converting NoneMoney to int"

def test_none_money_equality():
    none_money1 = NoneMoney()
    none_money2 = NoneMoney()
    assert none_money1 == none_money2, "Expected two undefined instances of NoneMoney to be equal"


if __name__ == "__main__":
    pytest.main()