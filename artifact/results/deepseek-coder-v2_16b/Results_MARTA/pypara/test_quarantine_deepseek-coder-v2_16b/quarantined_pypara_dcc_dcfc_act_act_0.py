
import pytest
from datetime import date, timedelta
from decimal import Decimal
import calendar
from pypara.dcc import dcfc_act_act

@pytest.mark.parametrize("start_date, asof_date, end_date, expected", [
    (date(2023, 1, 1), date(2023, 6, 30), date(2023, 12, 31), Decimal('0.58471442473239')),
])
def test_valid_case_1(start_date, asof_date, end_date, expected):
    result = dcfc_act_act(start=start_date, asof=asof_date, end=end_date)
    assert result == expected

@pytest.mark.parametrize("start_date, asof_date, end_date, expected", [
    (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('1.58471442473239')),
])
def test_valid_case_2(start_date, asof_date, end_date, expected):
    result = dcfc_act_act(start=start_date, asof=asof_date, end=end_date)
    assert result == expected

@pytest.mark.parametrize("start_date, asof_date, end_date", [
    (date(2024, 12, 31), date(2025, 1, 1), date(2025, 12, 31)),
])
def test_error_case(start_date, asof_date, end_date):
    with pytest.raises(ValueError):
        dcfc_act_act(start=start_date, asof=asof_date, end=end_date)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________ test_valid_case_1[start_date0-asof_date0-end_date0-expected0] _________

start_date = datetime.date(2023, 1, 1), asof_date = datetime.date(2023, 6, 30)
end_date = datetime.date(2023, 12, 31), expected = Decimal('0.58471442473239')

    @pytest.mark.parametrize("start_date, asof_date, end_date, expected", [
        (date(2023, 1, 1), date(2023, 6, 30), date(2023, 12, 31), Decimal('0.58471442473239')),
    ])
    def test_valid_case_1(start_date, asof_date, end_date, expected):
        result = dcfc_act_act(start=start_date, asof=asof_date, end=end_date)
>       assert result == expected
E       AssertionError: assert Decimal('0.4931506849315068493150684932') == Decimal('0.58471442473239')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py:13: AssertionError
________ test_valid_case_2[start_date0-asof_date0-end_date0-expected0] _________

start_date = datetime.date(2023, 1, 1), asof_date = datetime.date(2024, 6, 30)
end_date = datetime.date(2025, 12, 31), expected = Decimal('1.58471442473239')

    @pytest.mark.parametrize("start_date, asof_date, end_date, expected", [
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('1.58471442473239')),
    ])
    def test_valid_case_2(start_date, asof_date, end_date, expected):
        result = dcfc_act_act(start=start_date, asof=asof_date, end=end_date)
>       assert result == expected
E       AssertionError: assert Decimal('1.494535519125683060109289618') == Decimal('1.58471442473239')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py:20: AssertionError
______________ test_error_case[start_date0-asof_date0-end_date0] _______________

start_date = datetime.date(2024, 12, 31), asof_date = datetime.date(2025, 1, 1)
end_date = datetime.date(2025, 12, 31)

    @pytest.mark.parametrize("start_date, asof_date, end_date", [
        (date(2024, 12, 31), date(2025, 1, 1), date(2025, 12, 31)),
    ])
    def test_error_case(start_date, asof_date, end_date):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py:26: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py::test_valid_case_1[start_date0-asof_date0-end_date0-expected0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py::test_valid_case_2[start_date0-asof_date0-end_date0-expected0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_0.py::test_error_case[start_date0-asof_date0-end_date0]
============================== 3 failed in 0.07s ===============================
"""