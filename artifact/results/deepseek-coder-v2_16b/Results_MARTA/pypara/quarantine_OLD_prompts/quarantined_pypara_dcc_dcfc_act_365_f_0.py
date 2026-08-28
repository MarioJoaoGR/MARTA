
import pytest
from datetime import date, timedelta
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import dcfc_act_365_f




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_f_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        valid_dates = (date(2023, 1, 1), date(2023, 1, 1), date(2023, 6, 30))
        result = dcfc_act_365_f(*valid_dates)
        assert isinstance(result, Decimal), "Result should be a Decimal"
>       assert result == Decimal('0.49315068493151'), f"Expected 0.49315068493151 but got {result}"
E       AssertionError: Expected 0.49315068493151 but got 0
E       assert Decimal('0') == Decimal('0.49315068493151')
E        +  where Decimal('0.49315068493151') = Decimal('0.49315068493151')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_f_0.py:12: AssertionError
______________________________ test_invalid_dates ______________________________

    def test_invalid_dates():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_f_0.py:15: Failed
_____________________________ test_leap_year_case ______________________________

    def test_leap_year_case():
        with patch('pypara.dcc._get_actual_day_count', return_value=184):  # 184 days in period including leap year
            result = dcfc_act_365_f(date(2024, 1, 1), date(2024, 1, 1), date(2024, 6, 30))
            assert isinstance(result, Decimal), "Result should be a Decimal"
>           assert result == Decimal('0.5'), f"Expected 0.5 but got {result}"
E           AssertionError: Expected 0.5 but got 0.5041095890410958904109589041
E           assert Decimal('0.5041095890410958904109589041') == Decimal('0.5')
E            +  where Decimal('0.5') = Decimal('0.5')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_f_0.py:23: AssertionError
___________________________ test_non_leap_year_case ____________________________

    def test_non_leap_year_case():
        with patch('pypara.dcc._get_actual_day_count', return_value=183):  # 183 days in period without leap year
            result = dcfc_act_365_f(date(2023, 1, 1), date(2023, 1, 1), date(2023, 6, 30))
            assert isinstance(result, Decimal), "Result should be a Decimal"
>           assert result == Decimal('0.4986301369863'), f"Expected 0.4986301369863 but got {result}"
E           AssertionError: Expected 0.4986301369863 but got 0.5013698630136986301369863014
E           assert Decimal('0.5013698630136986301369863014') == Decimal('0.4986301369863')
E            +  where Decimal('0.4986301369863') = Decimal('0.4986301369863')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_f_0.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_f_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_f_0.py::test_invalid_dates
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_f_0.py::test_leap_year_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_365_f_0.py::test_non_leap_year_case
============================== 4 failed in 0.10s ===============================
"""