
import pytest
from unittest.mock import patch
import datetime
from decimal import Decimal
from pypara.dcc import _next_payment_date

def test_annual_payments():
    start = datetime.date(2023, 1, 1)
    frequency = 1
    eom = None
    
    with patch('pypara.dcc._next_payment_date', return_value=datetime.date(2024, 1, 1)):
        next_payment = _next_payment_date(start, frequency, eom)
        assert next_payment == datetime.date(2024, 1, 1)

def test_monthly_payments():
    start = datetime.date(2023, 1, 15)
    frequency = 12
    eom = None
    
    with patch('pypara.dcc._next_payment_date', return_value=datetime.date(2023, 2, 15)):
        next_payment = _next_payment_date(start, frequency, eom)
        assert next_payment == datetime.date(2023, 2, 15)

def test_specific_end_of_month():
    start = datetime.date(2023, 1, 31)
    frequency = 1
    eom = 31
    
    with patch('pypara.dcc._next_payment_date', return_value=datetime.date(2024, 1, 31)):
        next_payment = _next_payment_date(start, frequency, eom)
        assert next_payment == datetime.date(2024, 1, 31)

def test_quarterly_payments_with_end_of_month():
    start = datetime.date(2023, 1, 31)
    frequency = 4
    eom = 31
    
    with patch('pypara.dcc._next_payment_date', return_value=datetime.date(2023, 4, 30)):
        next_payment = _next_payment_date(start, frequency, eom)
        assert next_payment == datetime.date(2023, 4, 30)
