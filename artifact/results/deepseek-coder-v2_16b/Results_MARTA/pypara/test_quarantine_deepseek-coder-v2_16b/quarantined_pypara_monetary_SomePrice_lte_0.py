
import pytest
from pypara.monetary import SomePrice, IncompatibleCurrencyError



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_lte_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_valid_case_same_currency _________________________

    def test_valid_case_same_currency():
>       price1 = SomePrice(qty=100, ccy='USD')
E       TypeError: SomePrice.__new__() missing 1 required positional argument: 'dov'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_lte_0.py:6: TypeError
______________________ test_error_case_different_currency ______________________

    def test_error_case_different_currency():
        with pytest.raises(IncompatibleCurrencyError):
>           price1 = SomePrice(qty=100, ccy='USD')
E           TypeError: SomePrice.__new__() missing 1 required positional argument: 'dov'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_lte_0.py:11: TypeError
_______________________ test_error_case_undefined_price ________________________

    def test_error_case_undefined_price():
        with pytest.raises(IncompatibleCurrencyError):
>           price1 = SomePrice(qty=None, ccy='USD')
E           TypeError: SomePrice.__new__() missing 1 required positional argument: 'dov'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_lte_0.py:17: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_lte_0.py::test_valid_case_same_currency
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_lte_0.py::test_error_case_different_currency
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_SomePrice_lte_0.py::test_error_case_undefined_price
============================== 3 failed in 0.07s ===============================
"""