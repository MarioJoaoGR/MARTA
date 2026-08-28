
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import _next_payment_date



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__next_payment_date_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________ test_valid_case_specific_end_of_month _____________________

    def test_valid_case_specific_end_of_month():
        fixed_start = date(2023, 1, 1)
        next_payment = _next_payment_date(fixed_start, 1, 31)
>       assert next_payment == date(2023, 1, 31)
E       assert datetime.date(2024, 1, 31) == datetime.date(2023, 1, 31)
E        +  where datetime.date(2023, 1, 31) = date(2023, 1, 31)

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__next_payment_date_0.py:10: AssertionError
__________________________ test_edge_case_invalid_eom __________________________

    def test_edge_case_invalid_eom():
        fixed_start = date(2023, 1, 31)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__next_payment_date_0.py:14: Failed
____________________ test_invalid_input_negative_frequency _____________________

    def test_invalid_input_negative_frequency():
        fixed_start = date(2023, 1, 1)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__next_payment_date_0.py:19: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__next_payment_date_0.py::test_valid_case_specific_end_of_month
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__next_payment_date_0.py::test_edge_case_invalid_eom
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__next_payment_date_0.py::test_invalid_input_negative_frequency
============================== 3 failed in 0.07s ===============================
"""