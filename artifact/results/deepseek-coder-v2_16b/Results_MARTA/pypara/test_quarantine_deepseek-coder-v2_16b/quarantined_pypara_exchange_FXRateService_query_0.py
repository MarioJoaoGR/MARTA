
import pytest
from datetime import date
from pypara.currencies import Currency
from pypara.exchange import FXRateService, ConcreteFXRateService
from decimal import Decimal

# Test for querying a single foreign exchange rate
def test_query_single_fx_rate():
    fx_service = ConcreteFXRateService()
    ccy1 = Currency('USD')
    ccy2 = Currency('EUR')
    asof = date(2023, 4, 1)
    strict = False
    
    rate = fx_service.query(ccy1, ccy2, asof, strict)
    
    assert isinstance(rate, FXRate), "Expected a FXRate instance"
    if rate is not None:
        assert isinstance(rate.value, Decimal), "Expected the value to be a Decimal"

# Test for querying multiple foreign exchange rates
def test_query_multiple_fx_rates():
    fx_service = ConcreteFXRateService()
    queries = [
        (Currency('USD'), Currency('EUR'), date(2023, 4, 1)),
        (Currency('GBP'), Currency('USD'), date(2023, 4, 1))
    ]
    strict = False
    
    rates = fx_service.queries(queries, strict)
    
    assert len(rates) == 2, "Expected two FXRate instances"
    for rate in rates:
        if rate is not None:
            assert isinstance(rate.value, Decimal), "Expected the value to be a Decimal"

# Test for querying with strict mode
def test_query_strict_mode():
    fx_service = ConcreteFXRateService()
    ccy1 = Currency('USD')
    ccy2 = Currency('EUR')
    asof = date(2023, 4, 1)
    strict = True
    
    with pytest.raises(LookupError):
        fx_service.query(ccy1, ccy2, asof, strict)

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
________ ERROR collecting test_pypara_exchange_FXRateService_query_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_query_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_query_0.py:5: in <module>
    from pypara.exchange import FXRateService, ConcreteFXRateService
E   ImportError: cannot import name 'ConcreteFXRateService' from 'pypara.exchange' (/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/exchange.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_query_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""