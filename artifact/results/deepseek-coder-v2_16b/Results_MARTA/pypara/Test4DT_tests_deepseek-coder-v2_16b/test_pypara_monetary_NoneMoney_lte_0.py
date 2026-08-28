
import pytest
from pypara.monetary import NoneMoney, Money


def test_undefined_comparison():
    money1 = NoneMoney()
    money2 = NoneMoney()
    assert bool(money1) is False, "NoneMoney should be false in boolean context"
    assert (money1 < money2) is False, "Undefined values are not comparable"
    assert (money1 <= money2) is True, "Undefined values are considered equal"
    assert (money1 > money2) is False, "Undefined values are not comparable"
    assert (money1 >= money2) is True, "Undefined values are considered equal"

def test_conversion_methods():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        float(nm)
    with pytest.raises(TypeError):
        int(nm)
