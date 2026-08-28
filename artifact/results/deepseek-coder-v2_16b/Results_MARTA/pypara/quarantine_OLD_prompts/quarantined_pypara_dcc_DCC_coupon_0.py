
import pytest
from unittest.mock import patch, MagicMock
from pypara.dccclass import DCC, Currency, Money, Date, DCFC
import datetime
from decimal import Decimal

# Test 1: Basic Coupon Calculation
def test_basic_coupon_calculation():
    dcc = DCC()
    principal = Money('USD', Decimal('1000'))
    rate = Decimal('0.05')
    start_date = datetime.date(2023, 1, 1)
    asof_date = datetime.date.today()
    end_date = datetime.date(2023, 12, 31)
    freq = 12
    eom = None
    
    with patch('pypara.dccclass._last_payment_date', return_value=datetime.date(2023, 1, 1)):
        with patch('pypara.dccclass._next_payment_date', return_value=datetime.date(2023, 12, 31)):
            coupon_interest = dcc.coupon(principal, rate, start_date, asof_date, end_date, freq, eom)
    
    assert isinstance(coupon_interest, Money), "Expected a Money object"
    assert coupon_interest.amount == Decimal('50'), "Incorrect accrued interest calculated"

# Test 2: Default End Date Calculation
def test_default_end_date():
    dcc = DCC()
    principal = Money('USD', Decimal('1000'))
    rate = Decimal('0.05')
    start_date = datetime.date(2023, 1, 1)
    asof_date = datetime.date.today()
    freq = 12
    eom = None
    
    with patch('pypara.dccclass._last_payment_date', return_value=datetime.date(2023, 1, 1)):
        coupon_interest = dcc.coupon(principal, rate, start_date, asof_date, end_date=None, freq=freq, eom=eom)
    
    assert isinstance(coupon_interest, Money), "Expected a Money object"
    assert coupon_interest.amount == Decimal('50'), "Incorrect accrued interest calculated"

# Test 3: Specific End Date Calculation
def test_specific_end_date():
    dcc = DCC()
    principal = Money('USD', Decimal('1000'))
    rate = Decimal('0.05')
    start_date = datetime.date(2023, 1, 1)
    asof_date = datetime.date.today()
    end_date = datetime.date(2023, 4, 1)
    freq = 12
    eom = None
    
    with patch('pypara.dccclass._last_payment_date', return_value=datetime.date(2023, 1, 1)):
        coupon_interest = dcc.coupon(principal, rate, start_date, asof_date, end_date, freq, eom)
    
    assert isinstance(coupon_interest, Money), "Expected a Money object"
    assert coupon_interest.amount == Decimal('25'), "Incorrect accrued interest calculated"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______________ ERROR collecting test_pypara_dcc_DCC_coupon_0.py _______________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCC_coupon_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCC_coupon_0.py:4: in <module>
    from pypara.dccclass import DCC, Currency, Money, Date, DCFC
E   ModuleNotFoundError: No module named 'pypara.dccclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_DCC_coupon_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""