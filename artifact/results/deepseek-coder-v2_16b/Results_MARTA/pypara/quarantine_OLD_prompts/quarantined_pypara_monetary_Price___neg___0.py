
import pytest
from decimal import Decimal
from datetime import date
from currency import Currency
from pypara.monetary import Price

# Test case for initializing a Price object with valid parameters
def test_price_initialization():
    price = Price(ccy=Currency('USD'), qty=Decimal('100.25'), dov=date(2023, 4, 1))
    assert isinstance(price, Price)
    assert price.ccy == Currency('USD')
    assert price.qty == Decimal('100.25')
    assert price.dov == date(2023, 4, 1)
    assert price.defined is True
    assert price.undefined is False

# Test case for initializing an undefined Price object
def test_price_initialization_undefined():
    undefined_price = Price.of(ccy=Currency('USD'), qty=None, dov=date(2023, 4, 1))
    assert isinstance(undefined_price, Price)
    assert undefined_price.ccy == Currency('USD')
    assert undefined_price.qty is None
    assert undefined_price.dov == date(2023, 4, 1)
    assert bool(undefined_price) is False

# Test case for converting a defined price to another currency
def test_price_convert():
    price = Price(ccy=Currency('USD'), qty=Decimal('100.25'), dov=date(2023, 4, 1))
    converted_price = price.convert(to=Currency('EUR'))
    assert isinstance(converted_price, Price)
    assert converted_price.ccy == Currency('EUR')
    assert converted_price.qty != Decimal('100.25')  # Assuming conversion changes the quantity
    assert converted_price.dov == date(2023, 4, 1)

# Test case for negating a Price object
def test_price_negation():
    price = Price(ccy=Currency('USD'), qty=Decimal('100.25'), dov=date(2023, 4, 1))
    neg_price = -price
    assert isinstance(neg_price, Price)
    assert neg_price.ccy == Currency('USD')
    assert neg_price.qty == Decimal('-100.25')
    assert neg_price.dov == date(2023, 4, 1)
    assert neg_price.defined is True
    assert neg_price.undefined is False

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
___________ ERROR collecting test_pypara_monetary_Price___neg___0.py ___________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_Price___neg___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_Price___neg___0.py:5: in <module>
    from currency import Currency
E   ModuleNotFoundError: No module named 'currency'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_Price___neg___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""