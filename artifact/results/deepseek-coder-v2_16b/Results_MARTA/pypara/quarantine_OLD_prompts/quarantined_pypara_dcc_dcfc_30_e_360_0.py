
import pytest
from datetime import date, timedelta
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import dcfc_30_e_360

# Test for basic scenario without adjustments

# Test for scenario where `asof` is just after the end of a month (no adjustment needed)

# Test for scenario where `start` is the 31st of a month (adjust to 30th)

# Test for scenario where both `start` and `asof` are the 31st of a month (adjust accordingly)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_e_360_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
___________________________ test_dcfc_30_e_360_basic ___________________________

    def test_dcfc_30_e_360_basic():
        ex1_start = date(2007, 12, 28)
        ex1_asof = date(2008, 2, 28)
        with patch('pypara.dcc.datetime') as mock_datetime:
            mock_datetime.date.today.return_value = ex1_asof + timedelta(days=30)
>           assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof), 14) == Decimal('0.16666666666667')
E           TypeError: dcfc_30_e_360() missing 1 required positional argument: 'end'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_e_360_0.py:14: TypeError
_______________________ test_dcfc_30_e_360_no_adjustment _______________________

    def test_dcfc_30_e_360_no_adjustment():
        ex2_start = date(2007, 12, 28)
        ex2_asof = date(2008, 2, 29)
        with patch('pypara.dcc.datetime') as mock_datetime:
            mock_datetime.date.today.return_value = ex2_asof + timedelta(days=30)
>           assert round(dcfc_30_e_360(start=ex2_start, asof=ex2_asof), 14) == Decimal('0.16944444444444')
E           TypeError: dcfc_30_e_360() missing 1 required positional argument: 'end'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_e_360_0.py:22: TypeError
_______________________ test_dcfc_30_e_360_adjust_start ________________________

    def test_dcfc_30_e_360_adjust_start():
        ex3_start = date(2007, 10, 31)
        ex3_asof = date(2008, 11, 30)
        with patch('pypara.dcc.datetime') as mock_datetime:
            mock_datetime.date.today.return_value = ex3_asof + timedelta(days=30)
>           assert round(dcfc_30_e_360(start=ex3_start, asof=ex3_asof), 14) == Decimal('1.08333333333333')
E           TypeError: dcfc_30_e_360() missing 1 required positional argument: 'end'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_e_360_0.py:30: TypeError
________________________ test_dcfc_30_e_360_adjust_both ________________________

    def test_dcfc_30_e_360_adjust_both():
        ex4_start = date(2008, 2, 1)
        ex4_asof = date(2009, 5, 31)
        with patch('pypara.dcc.datetime') as mock_datetime:
            mock_datetime.date.today.return_value = ex4_asof + timedelta(days=365)
>           assert round(dcfc_30_e_360(start=ex4_start, asof=ex4_asof), 14) == Decimal('1.33055555555556')
E           TypeError: dcfc_30_e_360() missing 1 required positional argument: 'end'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_e_360_0.py:38: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_e_360_0.py::test_dcfc_30_e_360_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_e_360_0.py::test_dcfc_30_e_360_no_adjustment
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_e_360_0.py::test_dcfc_30_e_360_adjust_start
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_e_360_0.py::test_dcfc_30_e_360_adjust_both
============================== 4 failed in 0.09s ===============================
"""