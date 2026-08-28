
import pytest
from datetime import date
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import dcfc_act_365_l



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_l_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________ test_dcfc_act_365_l_standard_year _______________________

    def test_dcfc_act_365_l_standard_year():
        start = date(2023, 1, 1)
        asof = date(2023, 7, 1)
        end = date(2023, 12, 31)
        with patch('calendar.isleap', return_value=False):
            result = dcfc_act_365_l(start, asof, end)
>           assert round(result, 14) == Decimal('0.5')
E           AssertionError: assert Decimal('0.49589041095890') == Decimal('0.5')
E            +  where Decimal('0.49589041095890') = round(Decimal('0.4958904109589041095890410959'), 14)
E            +  and   Decimal('0.5') = Decimal('0.5')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_l_1.py:14: AssertionError
________________________ test_dcfc_act_365_l_leap_year _________________________

    def test_dcfc_act_365_l_leap_year():
        start = date(2024, 1, 1)
        asof = date(2024, 7, 1)
        end = date(2025, 6, 30)
        with patch('calendar.isleap', return_value=True):
            result = dcfc_act_365_l(start, asof, end)
>           assert round(result, 14) == Decimal('0.5')
E           AssertionError: assert Decimal('0.49726775956284') == Decimal('0.5')
E            +  where Decimal('0.49726775956284') = round(Decimal('0.4972677595628415300546448087'), 14)
E            +  and   Decimal('0.5') = Decimal('0.5')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_l_1.py:22: AssertionError
____________________ test_dcfc_act_365_l_with_optional_freq ____________________

    def test_dcfc_act_365_l_with_optional_freq():
        start = date(2023, 1, 1)
        asof = date(2023, 7, 1)
        end = date(2023, 12, 31)
        freq = Decimal('2')
        with patch('calendar.isleap', return_value=False):
            result = dcfc_act_365_l(start, asof, end, freq)
>           assert round(result, 14) == Decimal('0.5')
E           AssertionError: assert Decimal('0.49589041095890') == Decimal('0.5')
E            +  where Decimal('0.49589041095890') = round(Decimal('0.4958904109589041095890410959'), 14)
E            +  and   Decimal('0.5') = Decimal('0.5')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_l_1.py:31: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_l_1.py::test_dcfc_act_365_l_standard_year
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_l_1.py::test_dcfc_act_365_l_leap_year
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_l_1.py::test_dcfc_act_365_l_with_optional_freq
============================== 3 failed in 0.08s ===============================
"""