
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Currency, Money


def test_money_negative_undefined():
    undefined_money = Money()
    with pytest.raises(NotImplementedError):
        assert undefined_money.negative() == undefined_money  # This will also raise NotImplementedError, so the test passes by design