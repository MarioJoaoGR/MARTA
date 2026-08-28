
import pytest
from pypara.monetary import NoneMoney, Currency, Date



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_convert_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_conversion __________________________

    def test_valid_input_conversion():
        nm = NoneMoney()
>       converted = nm.convert(Currency.USD)
E       AttributeError: type object 'Currency' has no attribute 'USD'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_convert_1.py:7: AttributeError
__________________________ test_edge_case_none_inputs __________________________

    def test_edge_case_none_inputs():
        nm = NoneMoney()
>       to_currency = Currency.USD
E       AttributeError: type object 'Currency' has no attribute 'USD'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_convert_1.py:12: AttributeError
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        nm = NoneMoney()
        to_currency = 'INVALID_CURRENCY'
        asof_date = Date(2023, 4, 1)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_convert_1.py:19: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_convert_1.py::test_valid_input_conversion
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_convert_1.py::test_edge_case_none_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_monetary_NoneMoney_convert_1.py::test_invalid_input_error_handling
============================== 3 failed in 0.08s ===============================
"""