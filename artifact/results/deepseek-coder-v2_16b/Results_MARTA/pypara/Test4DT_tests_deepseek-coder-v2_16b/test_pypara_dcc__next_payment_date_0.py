
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import _next_payment_date

def test_next_payment_date_annual():
    start = date(2023, 1, 1)
    frequency = 1
    eom = None
    expected_date = date(2024, 1, 1)
    assert _next_payment_date(start, frequency, eom) == expected_date

def test_next_payment_date_monthly():
    start = date(2023, 1, 15)
    frequency = 12
    eom = None
    expected_date = date(2023, 2, 15)
    assert _next_payment_date(start, frequency, eom) == expected_date

def test_next_payment_date_specific_eom():
    start = date(2023, 1, 31)
    frequency = 1
    eom = 31
    expected_date = date(2024, 1, 31)
    assert _next_payment_date(start, frequency, eom) == expected_date

def test_next_payment_date_quarterly_eom():
    start = date(2023, 1, 31)
    frequency = 4
    eom = 31
    expected_date = date(2023, 4, 30)
    assert _next_payment_date(start, frequency, eom) == expected_date
