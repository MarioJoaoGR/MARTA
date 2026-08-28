
import pytest
from pypara.dcc import _get_date_range
import datetime


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__get_date_range_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_valid_date_range _____________________________

    def test_valid_date_range():
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2023, 1, 10)
        date_range = list(_get_date_range(start_date, end_date))
        expected_dates = [start_date + datetime.timedelta(days=i) for i in range(10)]
>       assert date_range == expected_dates
E       assert [datetime.dat...3, 1, 6), ...] == [datetime.dat...3, 1, 6), ...]
E         
E         Right contains one more item: datetime.date(2023, 1, 10)
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__get_date_range_0.py:11: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        start_date = datetime.date(2023, 1, 11)
        end_date = datetime.date(2023, 1, 1)
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__get_date_range_0.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__get_date_range_0.py::test_valid_date_range
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc__get_date_range_0.py::test_invalid_input
============================== 2 failed in 0.16s ===============================
"""