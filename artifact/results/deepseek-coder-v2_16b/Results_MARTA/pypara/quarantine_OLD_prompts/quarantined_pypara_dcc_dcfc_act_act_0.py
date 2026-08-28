
import pytest
from datetime import date, timedelta
from decimal import Decimal
import calendar
from unittest.mock import patch
from pypara.dcc import dcfc_act_act

def _get_date_range(start, end):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)

@pytest.mark.parametrize("start, asof, end", [
    (date(2023, 10, 31), date(2024, 11, 30), date(2023, 10, 31))
])
def test_error_case(start, asof, end):
    with pytest.raises(ValueError):
        dcfc_act_act(start=start, asof=asof, end=end)

@pytest.mark.parametrize("start, asof, end", [
    (date(2023, 1, 1), date(2023, 6, 30), date(2023, 12, 31))
])
def test_single_year_no_freq(start, asof, end):
    with patch('calendar.isleap', return_value=False):
        result = dcfc_act_act(start=start, asof=asof, end=end)
        assert isinstance(result, Decimal), "Result should be a Decimal"
        assert result == Decimal('0.5'), f"Expected 0.5 for single year no frequency adjustment but got {result}"

@pytest.mark.parametrize("start, asof, end", [
    (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31))
])
def test_multiple_years_including_leap(start, asof, end):
    with patch('calendar.isleap', side_effect=[False, True]):
        result = dcfc_act_act(start=start, asof=asof, end=end)
        assert isinstance(result, Decimal), "Result should be a Decimal"
        assert result == Decimal('1.5'), f"Expected 1.5 for multiple years including leap year but got {result}"

@pytest.mark.parametrize("start, asof, end, freq", [
    (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('2'))
])
def test_specified_frequency(start, asof, end, freq):
    with patch('calendar.isleap', side_effect=[False, True]):
        result = dcfc_act_act(start=start, asof=asof, end=end, freq=freq)
        assert isinstance(result, Decimal), "Result should be a Decimal"
        assert result == Decimal('1.5'), f"Expected 1.5 for specified frequency but got {result}"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
______________________ test_error_case[start0-asof0-end0] ______________________

start = datetime.date(2023, 10, 31), asof = datetime.date(2024, 11, 30)
end = datetime.date(2023, 10, 31)

    @pytest.mark.parametrize("start, asof, end", [
        (date(2023, 10, 31), date(2024, 11, 30), date(2023, 10, 31))
    ])
    def test_error_case(start, asof, end):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py:19: Failed
_________________ test_single_year_no_freq[start0-asof0-end0] __________________

start = datetime.date(2023, 1, 1), asof = datetime.date(2023, 6, 30)
end = datetime.date(2023, 12, 31)

    @pytest.mark.parametrize("start, asof, end", [
        (date(2023, 1, 1), date(2023, 6, 30), date(2023, 12, 31))
    ])
    def test_single_year_no_freq(start, asof, end):
        with patch('calendar.isleap', return_value=False):
            result = dcfc_act_act(start=start, asof=asof, end=end)
            assert isinstance(result, Decimal), "Result should be a Decimal"
>           assert result == Decimal('0.5'), f"Expected 0.5 for single year no frequency adjustment but got {result}"
E           AssertionError: Expected 0.5 for single year no frequency adjustment but got 0.4931506849315068493150684932
E           assert Decimal('0.4931506849315068493150684932') == Decimal('0.5')
E            +  where Decimal('0.5') = Decimal('0.5')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py:29: AssertionError
____________ test_multiple_years_including_leap[start0-asof0-end0] _____________

start = datetime.date(2023, 1, 1), asof = datetime.date(2024, 6, 30)
end = datetime.date(2025, 12, 31)

    @pytest.mark.parametrize("start, asof, end", [
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31))
    ])
    def test_multiple_years_including_leap(start, asof, end):
        with patch('calendar.isleap', side_effect=[False, True]):
            result = dcfc_act_act(start=start, asof=asof, end=end)
            assert isinstance(result, Decimal), "Result should be a Decimal"
>           assert result == Decimal('1.5'), f"Expected 1.5 for multiple years including leap year but got {result}"
E           AssertionError: Expected 1.5 for multiple years including leap year but got 1.494535519125683060109289618
E           assert Decimal('1.494535519125683060109289618') == Decimal('1.5')
E            +  where Decimal('1.5') = Decimal('1.5')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py:38: AssertionError
______________ test_specified_frequency[start0-asof0-end0-freq0] _______________

start = datetime.date(2023, 1, 1), asof = datetime.date(2024, 6, 30)
end = datetime.date(2025, 12, 31), freq = Decimal('2')

    @pytest.mark.parametrize("start, asof, end, freq", [
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('2'))
    ])
    def test_specified_frequency(start, asof, end, freq):
        with patch('calendar.isleap', side_effect=[False, True]):
            result = dcfc_act_act(start=start, asof=asof, end=end, freq=freq)
            assert isinstance(result, Decimal), "Result should be a Decimal"
>           assert result == Decimal('1.5'), f"Expected 1.5 for specified frequency but got {result}"
E           AssertionError: Expected 1.5 for specified frequency but got 1.494535519125683060109289618
E           assert Decimal('1.494535519125683060109289618') == Decimal('1.5')
E            +  where Decimal('1.5') = Decimal('1.5')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py:47: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py::test_error_case[start0-asof0-end0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py::test_single_year_no_freq[start0-asof0-end0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py::test_multiple_years_including_leap[start0-asof0-end0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py::test_specified_frequency[start0-asof0-end0-freq0]
============================== 4 failed in 0.09s ===============================
"""