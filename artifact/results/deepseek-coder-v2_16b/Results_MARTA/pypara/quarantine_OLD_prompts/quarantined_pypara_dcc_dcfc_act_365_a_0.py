
import pytest
from datetime import date, timedelta
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import dcfc_act_365_a, _get_actual_day_count, _has_leap_day




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________________ test_valid_case_standard_year _________________________

    def test_valid_case_standard_year():
        start = date(2023, 1, 1)
        asof = date(2023, 12, 31)
        end = date(2023, 12, 31)
    
        with patch('pypara.dcc._get_actual_day_count', return_value=Decimal('365')):
            result = dcfc_act_365_a(start, asof, end)
>           assert round(result, 14) == Decimal('0.9863')
E           AssertionError: assert Decimal('1.00000000000000') == Decimal('0.9863')
E            +  where Decimal('1.00000000000000') = round(Decimal('1'), 14)
E            +  and   Decimal('0.9863') = Decimal('0.9863')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py:15: AssertionError
________________________ test_valid_case_spanning_years ________________________

    def test_valid_case_spanning_years():
        start = date(2023, 10, 1)
        asof = date(2024, 5, 31)
        end = date(2024, 5, 31)
    
        with patch('pypara.dcc._get_actual_day_count', return_value=Decimal('246')):
            result = dcfc_act_365_a(start, asof, end)
>           assert round(result, 14) == Decimal('0.7213')
E           AssertionError: assert Decimal('0.67213114754098') == Decimal('0.7213')
E            +  where Decimal('0.67213114754098') = round(Decimal('0.6721311475409836065573770492'), 14)
E            +  and   Decimal('0.7213') = Decimal('0.7213')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py:24: AssertionError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        with pytest.raises(ValueError):
>           dcfc_act_365_a(start=None, asof=date(2023, 1, 1), end=date(2023, 12, 31))

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/dcc.py:545: in dcfc_act_365_a
    return _get_actual_day_count(start, asof) / Decimal(366 if _has_leap_day(start, asof) else 365)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

start = None, end = datetime.date(2023, 1, 1)

    def _get_actual_day_count(start: Date, end: Date) -> int:
        """
        Counts the actual number of days in the given period.
    
        :param start: The start date of the period.
        :param end: The end date of the period.
        :return: The number of days in the given period.
    
        >>> _get_actual_day_count(datetime.date(2017, 1, 1), datetime.date(2017, 1, 1))
        0
        >>> _get_actual_day_count(datetime.date(2017, 1, 1), datetime.date(2017, 1, 2))
        1
        """
>       return (end - start).days
E       TypeError: unsupported operand type(s) for -: 'datetime.date' and 'NoneType'

/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/dcc.py:55: TypeError
_______________________________ test_error_case ________________________________

    def test_error_case():
        with pytest.raises(ValueError):
>           dcfc_act_365_a(start='invalid', asof=date(2023, 1, 1), end=date(2023, 12, 31))

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/dcc.py:545: in dcfc_act_365_a
    return _get_actual_day_count(start, asof) / Decimal(366 if _has_leap_day(start, asof) else 365)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

start = 'invalid', end = datetime.date(2023, 1, 1)

    def _get_actual_day_count(start: Date, end: Date) -> int:
        """
        Counts the actual number of days in the given period.
    
        :param start: The start date of the period.
        :param end: The end date of the period.
        :return: The number of days in the given period.
    
        >>> _get_actual_day_count(datetime.date(2017, 1, 1), datetime.date(2017, 1, 1))
        0
        >>> _get_actual_day_count(datetime.date(2017, 1, 1), datetime.date(2017, 1, 2))
        1
        """
>       return (end - start).days
E       TypeError: unsupported operand type(s) for -: 'datetime.date' and 'str'

/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/dcc.py:55: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py::test_valid_case_standard_year
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py::test_valid_case_spanning_years
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py::test_error_case
============================== 4 failed in 0.12s ===============================
"""