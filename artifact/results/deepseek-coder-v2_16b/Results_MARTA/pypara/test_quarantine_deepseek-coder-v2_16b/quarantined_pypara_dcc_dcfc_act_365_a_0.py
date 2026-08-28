
import pytest
from decimal import Decimal
import datetime
from pypara.dcc import dcfc_act_365_a

def _has_leap_day(start, end):
    # Helper function to determine if there is a leap day in the period
    return start <= datetime.date(start.year, 2, 29) and end >= datetime.date(end.year, 2, 29)

def _get_actual_day_count(start, end):
    # Helper function to calculate the actual number of days between two dates
    return (end - start).days + 1

@pytest.fixture
def setup_standard_year():
    return datetime.date(2023, 1, 1), None, datetime.date(2023, 12, 31)

@pytest.fixture
def setup_leap_year():
    return datetime.date(2024, 1, 1), None, datetime.date(2024, 12, 31)

@pytest.fixture
def setup_invalid_input():
    return datetime.date(2024, 12, 31), None, datetime.date(2023, 12, 31)



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_valid_case_standard_year _________________________

setup_standard_year = (datetime.date(2023, 1, 1), None, datetime.date(2023, 12, 31))

    def test_valid_case_standard_year(setup_standard_year):
        start_date, _, end_date = setup_standard_year
        result = dcfc_act_365_a(start=start_date, asof=end_date, end=end_date)
        assert isinstance(result, Decimal), "Result should be a Decimal"
>       assert result == Decimal('0.9863'), f"Expected 0.9863 but got {result}"
E       AssertionError: Expected 0.9863 but got 0.9972602739726027397260273973
E       assert Decimal('0.9972602739726027397260273973') == Decimal('0.9863')
E        +  where Decimal('0.9863') = Decimal('0.9863')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py:31: AssertionError
__________________________ test_valid_case_leap_year ___________________________

setup_leap_year = (datetime.date(2024, 1, 1), None, datetime.date(2024, 12, 31))

    def test_valid_case_leap_year(setup_leap_year):
        start_date, _, end_date = setup_leap_year
        result = dcfc_act_365_a(start=start_date, asof=end_date, end=end_date)
        assert isinstance(result, Decimal), "Result should be a Decimal"
>       assert result == Decimal('1.0000'), f"Expected 1.0000 but got {result}"
E       AssertionError: Expected 1.0000 but got 0.9972677595628415300546448087
E       assert Decimal('0.9972677595628415300546448087') == Decimal('1.0000')
E        +  where Decimal('1.0000') = Decimal('1.0000')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py:37: AssertionError
___________________________ test_invalid_input_error ___________________________

setup_invalid_input = (datetime.date(2024, 12, 31), None, datetime.date(2023, 12, 31))

    def test_invalid_input_error(setup_invalid_input):
        start_date, _, end_date = setup_invalid_input
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py:41: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py::test_valid_case_standard_year
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py::test_valid_case_leap_year
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_a_0.py::test_invalid_input_error
============================== 3 failed in 0.08s ===============================
"""