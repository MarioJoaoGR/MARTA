
import pytest
from decimal import Decimal
import datetime
from unittest.mock import patch
from pypara.dcc import dcfc_nl_365, _get_actual_day_count, _has_leap_day


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
        start_date = datetime.date(2007, 12, 28)
        end_date = datetime.date(2008, 2, 28)
        with patch('pypara.dcc._get_actual_day_count', return_value=31):
            with patch('pypara.dcc._has_leap_day', return_value=False):
                result = dcfc_nl_365(start=start_date, asof=start_date, end=end_date)
                assert isinstance(result, Decimal), "Result should be a Decimal"
>               assert round(result, 14) == Decimal('0.16986301369863'), f"Expected Decimal('0.16986301369863'), but got {result}"
E               AssertionError: Expected Decimal('0.16986301369863'), but got 0.08493150684931506849315068493
E               assert Decimal('0.08493150684932') == Decimal('0.16986301369863')
E                +  where Decimal('0.08493150684932') = round(Decimal('0.08493150684931506849315068493'), 14)
E                +  and   Decimal('0.16986301369863') = Decimal('0.16986301369863')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py:15: AssertionError
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
        start_date = datetime.date(2007, 12, 28)
        end_date = datetime.date(2008, 2, 29)
        with patch('pypara.dcc._get_actual_day_count', return_value=31):
            with patch('pypara.dcc._has_leap_day', return_value=True):
                result = dcfc_nl_365(start=start_date, asof=start_date, end=end_date)
                assert isinstance(result, Decimal), "Result should be a Decimal"
>               assert round(result, 14) == Decimal('0.16986301369863'), f"Expected Decimal('0.16986301369863'), but got {result}"
E               AssertionError: Expected Decimal('0.16986301369863'), but got 0.08219178082191780821917808219
E               assert Decimal('0.08219178082192') == Decimal('0.16986301369863')
E                +  where Decimal('0.08219178082192') = round(Decimal('0.08219178082191780821917808219'), 14)
E                +  and   Decimal('0.16986301369863') = Decimal('0.16986301369863')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py::test_valid_case_1
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_nl_365_0.py::test_valid_case_2
============================== 2 failed in 0.09s ===============================
"""