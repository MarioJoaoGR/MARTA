
import pytest
from pypara.monetary import SomePrice, IncompatibleCurrencyError
from forex_currency import Currency, Date
from decimal import Decimal

# Test adding two defined prices with compatible currencies
def test_add_defined_prices_with_compatible_currencies():
    price1 = SomePrice(Currency('USD'), Decimal('100.50'), Date('2023-01-01'))
    price2 = SomePrice(Currency('USD'), Decimal('50.75'), Date('2023-01-01'))
    result_price = price1.add(price2)
    assert isinstance(result_price, SomePrice)
    assert result_price.currency == Currency('USD')
    assert result_price.amount == Decimal('151.25')
    assert result_price.date == Date('2023-01-01')

# Test adding a defined price to an undefined price
def test_add_defined_to_undefined():
    price1 = SomePrice(Currency('USD'), Decimal('100.50'), Date('2023-01-01'))
    price2 = NonePrice()  # Undefined price
    result_price = price1.add(price2)
    assert isinstance(result_price, SomePrice)
    assert result_price.currency == Currency('USD')
    assert result_price.amount == Decimal('100.50')
    assert result_price.date == Date('2023-01-01')

# Test adding two prices with different currencies, which should raise IncompatibleCurrencyError
def test_add_different_currencies():
    price1 = SomePrice(Currency('USD'), Decimal('100.50'), Date('2023-01-01'))
    price2 = SomePrice(Currency('EUR'), Decimal('50.75'), Date('2023-01-01'))
    with pytest.raises(IncompatibleCurrencyError):
        result_price = price1.add(price2)

# Test adding a defined price to another defined price with different currencies, which should raise IncompatibleCurrencyError
def test_add_defined_to_defined_different_currencies():
    price1 = SomePrice(Currency('USD'), Decimal('100.50'), Date('2023-01-01'))
    price2 = SomePrice(Currency('EUR'), Decimal('50.75'), Date('2023-01-01'))
    with pytest.raises(IncompatibleCurrencyError):
        result_price = price1.add(price2)

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
___________ ERROR collecting test_pypara_monetary_SomePrice_add_0.py ___________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_add_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_add_0.py:4: in <module>
    from forex_currency import Currency, Date
E   ModuleNotFoundError: No module named 'forex_currency'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_add_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""