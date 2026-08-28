
import pytest
from pypara.monetary import SomePrice, Currency, Date
from forex_currency import FXRateService, FXRateLookupError, ProgrammingError

# Test for converting USD to EUR
def test_convert_price_usd_to_eur():
    price = SomePrice(Currency('USD'), 100.50)
    converted_price = price.convert(Currency('EUR'), asof=Date(2023, 1, 1), strict=False)
    assert isinstance(converted_price, SomePrice)
    assert converted_price.currency == Currency('EUR')
    assert pytest.approx(converted_price.quantity) == 85.42  # Assuming the conversion rate is accurate for this example

# Test for converting USD to GBP without specifying a date
def test_convert_price_usd_to_gbp_without_date():
    price = SomePrice(Currency('USD'), 150.75)
    converted_price = price.convert(Currency('GBP'))
    assert isinstance(converted_price, SomePrice)
    assert converted_price.currency == Currency('GBP')
    assert pytest.approx(converted_price.quantity) == 125.63  # Assuming the conversion rate is accurate for this example

# Test for converting USD to JPY with strict mode enabled
def test_convert_price_usd_to_jpy_strict():
    price = SomePrice(Currency('USD'), 200.0)
    converted_price = price.convert(Currency('JPY'), asof=Date(2023, 1, 1), strict=True)
    assert isinstance(converted_price, SomePrice)
    assert converted_price.currency == Currency('JPY')
    assert pytest.approx(converted_price.quantity) == 24500  # Assuming the conversion rate is accurate for this example

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
_________ ERROR collecting test_pypara_monetary_SomePrice_convert_0.py _________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_convert_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_convert_0.py:4: in <module>
    from forex_currency import FXRateService, FXRateLookupError, ProgrammingError
E   ModuleNotFoundError: No module named 'forex_currency'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_convert_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""