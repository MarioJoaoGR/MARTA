
import pytest
from pypara.monetary import Money, Currency, Date


def test_invalid_input():
    money_instance = Money()
    with pytest.raises(NotImplementedError):
        money_instance.as_float()