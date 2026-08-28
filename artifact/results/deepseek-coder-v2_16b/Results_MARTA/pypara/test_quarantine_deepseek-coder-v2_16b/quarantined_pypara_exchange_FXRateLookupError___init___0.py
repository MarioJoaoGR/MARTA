
import pytest
from datetime import date
from pypara.exchange import Currency, FXRateLookupError


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateLookupError___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_fxratelookuperror_init_valid _______________________

    def test_fxratelookuperror_init_valid():
>       ccy1 = Currency('USD')
E       TypeError: Currency.__init__() missing 5 required positional arguments: 'name', 'decimals', 'type', 'quantizer', and 'hashcache'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateLookupError___init___0.py:7: TypeError
_____________________ test_fxratelookuperror_init_invalid ______________________

    def test_fxratelookuperror_init_invalid():
        ccy1 = "USD"
        ccy2 = "EUR"
        asof = date(2023, 1, 1)
    
        with pytest.raises(TypeError):
>           raise FXRateLookupError(ccy1, ccy2, asof)
E           pypara.exchange.FXRateLookupError: Foreign exchange rate for USD/EUR not found as of 2023-01-01

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateLookupError___init___0.py:22: FXRateLookupError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateLookupError___init___0.py::test_fxratelookuperror_init_valid
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_exchange_FXRateLookupError___init___0.py::test_fxratelookuperror_init_invalid
============================== 2 failed in 0.08s ===============================
"""