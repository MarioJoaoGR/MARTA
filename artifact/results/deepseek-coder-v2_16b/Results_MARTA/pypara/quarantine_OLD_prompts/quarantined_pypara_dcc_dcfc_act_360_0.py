
import pytest
from datetime import date, timedelta
from unittest.mock import patch
from pypara.dcc import dcfc_act_360



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_360_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
        start = date(2007, 12, 28)
        end = date(2008, 2, 28)
        with patch('pypara.dcc._get_actual_day_count', return_value=timedelta(days=60)):
>           result = dcfc_act_360(start=start, end=end)
E           TypeError: dcfc_act_360() missing 1 required positional argument: 'asof'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_360_0.py:11: TypeError
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
        start = date(2007, 12, 28)
        end = date(2008, 2, 29)
        with patch('pypara.dcc._get_actual_day_count', return_value=timedelta(days=61)):
>           result = dcfc_act_360(start=start, end=end)
E           TypeError: dcfc_act_360() missing 1 required positional argument: 'asof'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_360_0.py:18: TypeError
______________________________ test_valid_case_3 _______________________________

    def test_valid_case_3():
        start = date(2007, 10, 31)
        end = date(2008, 11, 30)
        with patch('pypara.dcc._get_actual_day_count', return_value=timedelta(days=395)):
>           result = dcfc_act_360(start=start, end=end)
E           TypeError: dcfc_act_360() missing 1 required positional argument: 'asof'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_360_0.py:25: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_360_0.py::test_valid_case_1
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_360_0.py::test_valid_case_2
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_360_0.py::test_valid_case_3
============================== 3 failed in 0.08s ===============================
"""