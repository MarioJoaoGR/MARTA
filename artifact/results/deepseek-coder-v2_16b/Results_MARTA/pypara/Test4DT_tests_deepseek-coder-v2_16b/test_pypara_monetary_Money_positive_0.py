
import pytest
from pypara.monetary import Money, Currency, Date


def test_positive_method_not_implemented():
    money = Money()
    with pytest.raises(NotImplementedError):
        money.positive()
