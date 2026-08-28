
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_30_360_us

def _is_last_day_of_month(date):
    # Helper function to check if a date is the last day of the month
    if date.day == 31 or (date.day in [30, 29, 28] and date.month in [4, 6, 9, 11]):
        return True
    return False



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_us_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        start_date = date(2007, 12, 28)
        asof_date = date(2008, 2, 28)
        end_date = date(2008, 2, 28)
        result = dcfc_30_360_us(start=start_date, asof=asof_date, end=end_date)
>       assert Decimal('0.16666666666667') == pytest.approx(result, rel=1e-12)

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_us_1.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/data/pydeps/marta/_pytest/python_api.py:459: in __eq__
    result: bool = abs(self.expected - actual) <= self.tolerance
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[TypeError("unsupported operand type(s) for *: 'float' and 'decimal.Decimal'") raised in repr()] ApproxDecimal object at 0x7fc00fa2b100>

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
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        start_date = date(2007, 10, 31)
        asof_date = date(2008, 11, 30)
        end_date = date(2008, 11, 30)
        result = dcfc_30_360_us(start=start_date, asof=asof_date, end=end_date)
>       assert Decimal('1.08333333333333') == pytest.approx(result, rel=1e-12)

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_us_1.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/data/pydeps/marta/_pytest/python_api.py:459: in __eq__
    result: bool = abs(self.expected - actual) <= self.tolerance
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[TypeError("unsupported operand type(s) for *: 'float' and 'decimal.Decimal'") raised in repr()] ApproxDecimal object at 0x7fc00fa2be80>

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
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        start_date = None
        asof_date = date(2009, 5, 31)
        end_date = date(2009, 5, 31)
        with pytest.raises(TypeError):
>           dcfc_30_360_us(start=start_date, asof=asof_date, end=end_date)

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_us_1.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

start = None, asof = datetime.date(2009, 5, 31)
end = datetime.date(2009, 5, 31), freq = None

    @dcc("30/360 US", {"30U/360", "30US/360"})
    def dcfc_30_360_us(start: Date, asof: Date, end: Date, freq: Optional[Decimal] = None) -> Decimal:
        """
        Computes the day count fraction for the "30/360 US" convention.
    
        :param start: The start date of the period.
        :param asof: The date which the day count fraction to be calculated as of.
        :param end: The end date of the period (a.k.a. termination date).
        :return: Day count fraction.
    
        >>> ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
        >>> ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
        >>> ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
        >>> ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
        >>> round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)
        Decimal('0.16666666666667')
        >>> round(dcfc_30_360_us(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14)
        Decimal('0.16944444444444')
        >>> round(dcfc_30_360_us(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14)
        Decimal('1.08333333333333')
        >>> round(dcfc_30_360_us(start=ex4_start, asof=ex4_asof, end=ex4_asof), 14)
        Decimal('1.33333333333333')
        """
        ## Get D1 and D2:
>       d1 = start.day
E       AttributeError: 'NoneType' object has no attribute 'day'

/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/dcc.py:781: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_us_1.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_us_1.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_us_1.py::test_invalid_inputs
============================== 3 failed in 0.10s ===============================
"""