
import pytest
from pypara.monetary import Currency, IncompatibleCurrencyError



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_IncompatibleCurrencyError___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________ test_incompatible_currency_error_default_operation ______________

    def test_incompatible_currency_error_default_operation():
>       ccy1 = Currency('USD')
E       TypeError: Currency.__init__() missing 5 required positional arguments: 'name', 'decimals', 'type', 'quantizer', and 'hashcache'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_IncompatibleCurrencyError___init___0.py:6: TypeError
_______________ test_incompatible_currency_error_with_operation ________________

    def test_incompatible_currency_error_with_operation():
>       ccy1 = Currency('USD')
E       TypeError: Currency.__init__() missing 5 required positional arguments: 'name', 'decimals', 'type', 'quantizer', and 'hashcache'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_IncompatibleCurrencyError___init___0.py:13: TypeError
_________________ test_incompatible_currency_error_attributes __________________

    def test_incompatible_currency_error_attributes():
>       ccy1 = Currency('USD')
E       TypeError: Currency.__init__() missing 5 required positional arguments: 'name', 'decimals', 'type', 'quantizer', and 'hashcache'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_IncompatibleCurrencyError___init___0.py:20: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_IncompatibleCurrencyError___init___0.py::test_incompatible_currency_error_default_operation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_IncompatibleCurrencyError___init___0.py::test_incompatible_currency_error_with_operation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_IncompatibleCurrencyError___init___0.py::test_incompatible_currency_error_attributes
============================== 3 failed in 0.09s ===============================
"""