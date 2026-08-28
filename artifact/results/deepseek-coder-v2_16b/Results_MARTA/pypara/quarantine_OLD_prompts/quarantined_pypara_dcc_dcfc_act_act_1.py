
import pytest
from datetime import date, timedelta
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import dcfc_act_act



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
        start = date(2023, 1, 1)
        asof = date(2023, 6, 30)
        end = date(2023, 12, 31)
        with patch('pypara.dcc.calendar.isleap', return_value=False):
            result = dcfc_act_act(start=start, asof=asof, end=end)
            assert isinstance(result, Decimal), "Result should be a Decimal"
>           assert result == Decimal('0.16942884946478'), f"Expected 0.16942884946478, but got {result}"
E           AssertionError: Expected 0.16942884946478, but got 0.4931506849315068493150684932
E           assert Decimal('0.4931506849315068493150684932') == Decimal('0.16942884946478')
E            +  where Decimal('0.16942884946478') = Decimal('0.16942884946478')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py:15: AssertionError
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
        start = date(2023, 1, 1)
        asof = date(2024, 6, 30)
        end = date(2025, 12, 31)
        with patch('pypara.dcc.calendar.isleap', return_value=False):
            result = dcfc_act_act(start=start, asof=asof, end=end)
            assert isinstance(result, Decimal), "Result should be a Decimal"
>           assert result == Decimal('0.17216108990194'), f"Expected 0.17216108990194, but got {result}"
E           AssertionError: Expected 0.17216108990194, but got 1.495890410958904109589041096
E           assert Decimal('1.495890410958904109589041096') == Decimal('0.17216108990194')
E            +  where Decimal('0.17216108990194') = Decimal('0.17216108990194')

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py:24: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        start = "2023-01-01"
        asof = date(2024, 6, 30)
        end = date(2025, 12, 31)
        with pytest.raises(TypeError):
>           dcfc_act_act(start=start, asof=asof, end=end)

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

start = '2023-01-01', asof = datetime.date(2024, 6, 30)
end = datetime.date(2025, 12, 31), freq = None

    @dcc("Act/Act", {"Actual/Actual", "Actual/Actual (ISDA)"})
    def dcfc_act_act(start: Date, asof: Date, end: Date, freq: Optional[Decimal] = None) -> Decimal:
        """
        Computes the day count fraction for "Act/Act" convention.
    
        :param start: The start date of the period.
        :param asof: The date which the day count fraction to be calculated as of.
        :param end: The end date of the period (a.k.a. termination date).
        :param freq: The frequency of payments in a year.
        :return: Day count fraction.
    
        >>> ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
        >>> ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
        >>> ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
        >>> ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
        >>> round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)
        Decimal('0.16942884946478')
        >>> round(dcfc_act_act(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14)
        Decimal('0.17216108990194')
        >>> round(dcfc_act_act(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14)
        Decimal('1.08243131970956')
        >>> round(dcfc_act_act(start=ex4_start, asof=ex4_asof, end=ex4_asof), 14)
        Decimal('1.32625945055768')
        """
        ## Get all years of interest by checking the leap year:
>       years = {year: calendar.isleap(year) for year in range(start.year, asof.year + 1)}
E       AttributeError: 'str' object has no attribute 'year'

/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/dcc.py:424: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py::test_valid_case_1
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py::test_valid_case_2
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py::test_invalid_input
============================== 3 failed in 0.09s ===============================
"""