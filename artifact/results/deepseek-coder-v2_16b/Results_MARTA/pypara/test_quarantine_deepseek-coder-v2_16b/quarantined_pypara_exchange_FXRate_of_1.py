
import pytest
from pypara.exchange import FXRateService, ConcreteFXRateService
from pypara.currencies import Currencies
from datetime import date
from decimal import Decimal

# Test valid case scenario
def test_valid_case():
    fx_service = ConcreteFXRateService()
    ccy1 = Currencies["USD"]
    ccy2 = Currencies["EUR"]
    asof_date = date(2023, 4, 1)
    rate = fx_service.query(ccy1, ccy2, asof_date, strict=True)
    
    assert rate is not None, "Rate should be found"
    assert isinstance(rate, FXRate), "Rate should be an instance of FXRate"
    assert rate.value == Decimal("2"), "The exchange rate value should be 2"

# Test edge case scenario
def test_edge_case():
    fx_service = ConcreteFXRateService()
    ccy1 = Currencies["USD"]
    ccy2 = Currencies["USD"]
    asof_date = date(2023, 4, 1)
    rate = fx_service.query(ccy1, ccy2, asof_date, strict=True)
    
    assert rate is not None, "Rate should be found"
    assert isinstance(rate, FXRate), "Rate should be an instance of FXRate"
    assert rate.value == Decimal("1"), "The exchange rate value to the same currency should be 1"

# Test invalid case scenario
def test_invalid_case():
    fx_service = ConcreteFXRateService()
    ccy1 = Currencies["USD"]
    ccy2 = Currencies["JPY"]  # Invalid currency pair
    asof_date = date(2023, 4, 1)
    rate = fx_service.query(ccy1, ccy2, asof_date, strict=True)
    
    assert rate is None, "Rate should not be found for invalid currency pair"

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
_____________ ERROR collecting test_pypara_exchange_FXRate_of_1.py _____________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate_of_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate_of_1.py:3: in <module>
    from pypara.exchange import FXRateService, ConcreteFXRateService
E   ImportError: cannot import name 'ConcreteFXRateService' from 'pypara.exchange' (/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/exchange.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRate_of_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""