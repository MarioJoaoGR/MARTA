
import pytest
from unittest.mock import patch, MagicMock
from pypara.exchange import FXRateService, Currency, Date, FXRate
from your_module import ConcreteFXRateService  # Replace 'your_module' with the actual module name where FXRateService is defined

# Test Case 1: Querying a Single FX Rate
def test_query_single_fx_rate():
    with patch('your_module.ConcreteFXRateService') as mock_service:
        # Arrange
        ccy1 = Currency('USD')
        ccy2 = Currency('EUR')
        asof = Date(2023, 4, 1)
        strict = False
        expected_rate = FXRate(Decimal('0.85'))
        mock_service.return_value.query.return_value = expected_rate
        
        # Act
        fx_service = ConcreteFXRateService()
        rate = fx_service.query(ccy1, ccy2, asof, strict)
        
        # Assert
        assert rate == expected_rate
        mock_service.return_value.query.assert_called_once_with(ccy1, ccy2, asof, strict)

# Test Case 2: Querying Multiple FX Rates
def test_query_multiple_fx_rates():
    with patch('your_module.ConcreteFXRateService') as mock_service:
        # Arrange
        queries = [(Currency('USD'), Currency('EUR'), Date(2023, 4, 1)), (Currency('GBP'), Currency('USD'), Date(2023, 4, 1))]
        strict = False
        expected_rates = [FXRate(Decimal('0.85')), FXRate(Decimal('1.37'))]
        mock_service.return_value.queries.return_value = expected_rates
        
        # Act
        fx_service = ConcreteFXRateService()
        rates = fx_service.queries(queries, strict)
        
        # Assert
        assert rates == expected_rates
        mock_service.return_value.queries.assert_called_once_with(queries, strict)

# Test Case 3: Querying FX Rate with Strict Mode
def test_query_fx_rate_strict():
    with patch('your_module.ConcreteFXRateService') as mock_service:
        # Arrange
        ccy1 = Currency('USD')
        ccy2 = Currency('EUR')
        asof = Date(2023, 4, 1)
        strict = True
        mock_service.return_value.query.side_effect = LookupError("Rate not found")
        
        # Act & Assert
        fx_service = ConcreteFXRateService()
        with pytest.raises(LookupError):
            fx_service.query(ccy1, ccy2, asof, strict)
        mock_service.return_value.query.assert_called_once_with(ccy1, ccy2, asof, strict)

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
    from your_module import ConcreteFXRateService  # Replace 'your_module' with the actual module name where FXRateService is defined
E   ModuleNotFoundError: No module named 'your_module'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateService_query_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""