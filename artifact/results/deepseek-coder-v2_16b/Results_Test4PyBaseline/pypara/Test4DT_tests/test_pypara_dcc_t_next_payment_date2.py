
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import _next_payment_date

# Test cases for _next_payment_date function
def test_basic_usage():
    start = date(2023, 1, 1)
    frequency = Decimal('1')
    eom = None
    
    next_date = _next_payment_date(start, frequency, eom)
    assert next_date == date(2024, 1, 1), f"Expected datetime.date(2024, 1, 1), but got {next_date}"

def test_specify_end_of_month():
    start = date(2023, 1, 15)
    frequency = Decimal('1')
    eom = 15
    
    next_date = _next_payment_date(start, frequency, eom)
    assert next_date == date(2024, 1, 15), f"Expected datetime.date(2024, 1, 15), but got {next_date}"

def test_different_frequency():
    start = date(2023, 1, 1)
    frequency = Decimal('0.5')  # Semi-annual payments
    eom = None
    
    next_date = _next_payment_date(start, frequency, eom)