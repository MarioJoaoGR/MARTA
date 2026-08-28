
import pytest
from datetime import date, timedelta
from decimal import Decimal
import calendar
from typing import List, Optional

# Assuming dcfc_act_act is defined in a module named pypara.dcc
from pypara.dcc import dcfc_act_act

def _get_date_range(start: date, end: date) -> List[date]:
    delta = end - start
    return [start + timedelta(days=i) for i in range(delta.days + 1)]

@pytest.mark.parametrize("start, asof, end, expected", [
    (date(2023, 1, 1), date(2023, 6, 30), date(2023, 12, 31), Decimal('0.5')),
    (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('1.5')),
    (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('1'))
])
def test_valid_case(start, asof, end, expected):
    result = dcfc_act_act(start=start, asof=asof, end=end)
    assert isinstance(result, Decimal), "Result should be a Decimal"
    assert result == pytest.approx(expected, rel=1e-9), f"Expected day count fraction for Act/Act is {expected}"


@pytest.mark.parametrize("start, asof, end", [
    (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31)),
    (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31))
])
def test_error_case_invalid_dates(start, asof, end):
    with pytest.raises(ValueError):
        dcfc_act_act(start=start, asof=asof, end=end)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 6 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py F [ 16%]
FFFFF                                                                    [100%]

=================================== FAILURES ===================================
_________________ test_valid_case[start0-asof0-end0-expected0] _________________

start = datetime.date(2023, 1, 1), asof = datetime.date(2023, 6, 30)
end = datetime.date(2023, 12, 31), expected = Decimal('0.5')

    @pytest.mark.parametrize("start, asof, end, expected", [
        (date(2023, 1, 1), date(2023, 6, 30), date(2023, 12, 31), Decimal('0.5')),
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('1.5')),
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('1'))
    ])
    def test_valid_case(start, asof, end, expected):
        result = dcfc_act_act(start=start, asof=asof, end=end)
        assert isinstance(result, Decimal), "Result should be a Decimal"
>       assert result == pytest.approx(expected, rel=1e-9), f"Expected day count fraction for Act/Act is {expected}"

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/data/pydeps/marta/_pytest/python_api.py:459: in __eq__
    result: bool = abs(self.expected - actual) <= self.tolerance
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[TypeError("unsupported operand type(s) for *: 'float' and 'decimal.Decimal'") raised in repr()] ApproxDecimal object at 0x7f670b088190>

    @property
    def tolerance(self):
        """Return the tolerance for the comparison.
    
        This could be either an absolute tolerance or a relative tolerance,
        depending on what the user specified or which would be larger.
        """
    
        def set_default(x, default):
            return x if x is not None else default
    
        # Figure out what the absolute tolerance should be.  ``self.abs`` is
        # either None or a value specified by the user.
        absolute_tolerance = set_default(self.abs, self.DEFAULT_ABSOLUTE_TOLERANCE)
    
        if absolute_tolerance < 0:
            raise ValueError(
                f"absolute tolerance can't be negative: {absolute_tolerance}"
            )
        if math.isnan(absolute_tolerance):
            raise ValueError("absolute tolerance can't be NaN.")
    
        # If the user specified an absolute tolerance but not a relative one,
        # just return the absolute tolerance.
        if self.rel is None:
            if self.abs is not None:
                return absolute_tolerance
    
        # Figure out what the relative tolerance should be.  ``self.rel`` is
        # either None or a value specified by the user.  This is done after
        # we've made sure the user didn't ask for an absolute tolerance only,
        # because we don't want to raise errors about the relative tolerance if
        # we aren't even going to use it.
>       relative_tolerance = set_default(
            self.rel, self.DEFAULT_RELATIVE_TOLERANCE
        ) * abs(self.expected)
E       TypeError: unsupported operand type(s) for *: 'float' and 'decimal.Decimal'

/data/pydeps/marta/_pytest/python_api.py:498: TypeError
_________________ test_valid_case[start1-asof1-end1-expected1] _________________

start = datetime.date(2023, 1, 1), asof = datetime.date(2024, 6, 30)
end = datetime.date(2025, 12, 31), expected = Decimal('1.5')

    @pytest.mark.parametrize("start, asof, end, expected", [
        (date(2023, 1, 1), date(2023, 6, 30), date(2023, 12, 31), Decimal('0.5')),
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('1.5')),
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('1'))
    ])
    def test_valid_case(start, asof, end, expected):
        result = dcfc_act_act(start=start, asof=asof, end=end)
        assert isinstance(result, Decimal), "Result should be a Decimal"
>       assert result == pytest.approx(expected, rel=1e-9), f"Expected day count fraction for Act/Act is {expected}"

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/data/pydeps/marta/_pytest/python_api.py:459: in __eq__
    result: bool = abs(self.expected - actual) <= self.tolerance
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[TypeError("unsupported operand type(s) for *: 'float' and 'decimal.Decimal'") raised in repr()] ApproxDecimal object at 0x7f670b088250>

    @property
    def tolerance(self):
        """Return the tolerance for the comparison.
    
        This could be either an absolute tolerance or a relative tolerance,
        depending on what the user specified or which would be larger.
        """
    
        def set_default(x, default):
            return x if x is not None else default
    
        # Figure out what the absolute tolerance should be.  ``self.abs`` is
        # either None or a value specified by the user.
        absolute_tolerance = set_default(self.abs, self.DEFAULT_ABSOLUTE_TOLERANCE)
    
        if absolute_tolerance < 0:
            raise ValueError(
                f"absolute tolerance can't be negative: {absolute_tolerance}"
            )
        if math.isnan(absolute_tolerance):
            raise ValueError("absolute tolerance can't be NaN.")
    
        # If the user specified an absolute tolerance but not a relative one,
        # just return the absolute tolerance.
        if self.rel is None:
            if self.abs is not None:
                return absolute_tolerance
    
        # Figure out what the relative tolerance should be.  ``self.rel`` is
        # either None or a value specified by the user.  This is done after
        # we've made sure the user didn't ask for an absolute tolerance only,
        # because we don't want to raise errors about the relative tolerance if
        # we aren't even going to use it.
>       relative_tolerance = set_default(
            self.rel, self.DEFAULT_RELATIVE_TOLERANCE
        ) * abs(self.expected)
E       TypeError: unsupported operand type(s) for *: 'float' and 'decimal.Decimal'

/data/pydeps/marta/_pytest/python_api.py:498: TypeError
_________________ test_valid_case[start2-asof2-end2-expected2] _________________

start = datetime.date(2023, 1, 1), asof = datetime.date(2024, 6, 30)
end = datetime.date(2025, 12, 31), expected = Decimal('1')

    @pytest.mark.parametrize("start, asof, end, expected", [
        (date(2023, 1, 1), date(2023, 6, 30), date(2023, 12, 31), Decimal('0.5')),
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('1.5')),
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31), Decimal('1'))
    ])
    def test_valid_case(start, asof, end, expected):
        result = dcfc_act_act(start=start, asof=asof, end=end)
        assert isinstance(result, Decimal), "Result should be a Decimal"
>       assert result == pytest.approx(expected, rel=1e-9), f"Expected day count fraction for Act/Act is {expected}"

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/data/pydeps/marta/_pytest/python_api.py:459: in __eq__
    result: bool = abs(self.expected - actual) <= self.tolerance
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[TypeError("unsupported operand type(s) for *: 'float' and 'decimal.Decimal'") raised in repr()] ApproxDecimal object at 0x7f670af33be0>

    @property
    def tolerance(self):
        """Return the tolerance for the comparison.
    
        This could be either an absolute tolerance or a relative tolerance,
        depending on what the user specified or which would be larger.
        """
    
        def set_default(x, default):
            return x if x is not None else default
    
        # Figure out what the absolute tolerance should be.  ``self.abs`` is
        # either None or a value specified by the user.
        absolute_tolerance = set_default(self.abs, self.DEFAULT_ABSOLUTE_TOLERANCE)
    
        if absolute_tolerance < 0:
            raise ValueError(
                f"absolute tolerance can't be negative: {absolute_tolerance}"
            )
        if math.isnan(absolute_tolerance):
            raise ValueError("absolute tolerance can't be NaN.")
    
        # If the user specified an absolute tolerance but not a relative one,
        # just return the absolute tolerance.
        if self.rel is None:
            if self.abs is not None:
                return absolute_tolerance
    
        # Figure out what the relative tolerance should be.  ``self.rel`` is
        # either None or a value specified by the user.  This is done after
        # we've made sure the user didn't ask for an absolute tolerance only,
        # because we don't want to raise errors about the relative tolerance if
        # we aren't even going to use it.
>       relative_tolerance = set_default(
            self.rel, self.DEFAULT_RELATIVE_TOLERANCE
        ) * abs(self.expected)
E       TypeError: unsupported operand type(s) for *: 'float' and 'decimal.Decimal'

/data/pydeps/marta/_pytest/python_api.py:498: TypeError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        start = None
        asof = None
        end = None
        with pytest.raises(ValueError):
>           dcfc_act_act(start=start, asof=asof, end=end)

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

start = None, asof = None, end = None, freq = None

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
E       AttributeError: 'NoneType' object has no attribute 'year'

/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/dcc.py:424: AttributeError
_______________ test_error_case_invalid_dates[start0-asof0-end0] _______________

start = datetime.date(2023, 1, 1), asof = datetime.date(2024, 6, 30)
end = datetime.date(2025, 12, 31)

    @pytest.mark.parametrize("start, asof, end", [
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31)),
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31))
    ])
    def test_error_case_invalid_dates(start, asof, end):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py:37: Failed
_______________ test_error_case_invalid_dates[start1-asof1-end1] _______________

start = datetime.date(2023, 1, 1), asof = datetime.date(2024, 6, 30)
end = datetime.date(2025, 12, 31)

    @pytest.mark.parametrize("start, asof, end", [
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31)),
        (date(2023, 1, 1), date(2024, 6, 30), date(2025, 12, 31))
    ])
    def test_error_case_invalid_dates(start, asof, end):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py:37: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py::test_valid_case[start0-asof0-end0-expected0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py::test_valid_case[start1-asof1-end1-expected1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py::test_valid_case[start2-asof2-end2-expected2]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py::test_error_case_invalid_dates[start0-asof0-end0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_act_act_1.py::test_error_case_invalid_dates[start1-asof1-end1]
============================== 6 failed in 0.14s ===============================
"""