
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import _last_payment_date



def test_invalid_input_large_frequency():
    start_date = date(2014, 1, 1)
    asof_date = date(2015, 12, 31)
    frequency = Decimal('13')
    with pytest.raises(ValueError):
        _last_payment_date(start_date, asof_date, frequency)


def test_valid_input_monthly_payments():
    start_date = date(2014, 1, 1)
    asof_date = date(2015, 12, 31)
    frequency = Decimal('1')
    expected_date = date(2015, 1, 1)
    assert _last_payment_date(start_date, asof_date, frequency) == expected_date

def test_valid_input_bi_monthly_payments():
    start_date = date(2014, 1, 1)
    asof_date = date(2015, 12, 31)
    frequency = Decimal('2')
    expected_date = date(2015, 7, 1)
    assert _last_payment_date(start_date, asof_date, frequency) == expected_date
