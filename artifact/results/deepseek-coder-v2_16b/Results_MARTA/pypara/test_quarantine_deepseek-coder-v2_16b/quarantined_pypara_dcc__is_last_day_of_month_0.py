
import pytest
from datetime import datetime
import calendar
from pypara.dcc import _is_last_day_of_month


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__is_last_day_of_month_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        date = None
        with pytest.raises(TypeError):
>           _is_last_day_of_month(date)

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__is_last_day_of_month_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

date = None

    def _is_last_day_of_month(date: Date) -> bool:
        """
        Indicates if the date is the last day of the month.
        """
>       return date.day == calendar.monthrange(date.year, date.month)[1]
E       AttributeError: 'NoneType' object has no attribute 'day'

/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/dcc.py:83: AttributeError
_________________________ test_valid_last_day_of_month _________________________

    def test_valid_last_day_of_month():
        # Test for the last day of a month in a regular year
        date = datetime(2023, 10, 31)
        assert _is_last_day_of_month(date) == True
    
        # Test for the last day of February in a non-leap year
        date = datetime(2023, 2, 28)
>       assert _is_last_day_of_month(date) == False
E       assert True == False
E        +  where True = _is_last_day_of_month(datetime.datetime(2023, 2, 28, 0, 0))

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__is_last_day_of_month_0.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__is_last_day_of_month_0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__is_last_day_of_month_0.py::test_valid_last_day_of_month
============================== 2 failed in 0.07s ===============================
"""