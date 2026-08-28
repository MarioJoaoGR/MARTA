
import pytest
from datetime import date
from unittest.mock import patch
from pypara.dcc import dcfc_30_360_german


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_german_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_specific_date_adjustment _________________________

    def test_specific_date_adjustment():
        start = date(2007, 10, 31)
        asof = date(2008, 11, 30)
        end = date(2008, 11, 30)
    
        with patch('pypara.dcc._is_last_day_of_month', return_value=False):
            result = dcfc_30_360_german(start=start, asof=asof, end=end)
>           assert result == pytest.approx(1.08333333333333, rel=1e-12)

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_german_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = 1.08333333333333 ± 1.1e-12
actual = Decimal('1.083333333333333333333333333')

    def __eq__(self, actual) -> bool:
        """Return whether the given value is equal to the expected value
        within the pre-specified tolerance."""
        asarray = _as_numpy_array(actual)
        if asarray is not None:
            # Call ``__eq__()`` manually to prevent infinite-recursion with
            # numpy<1.13.  See #3748.
            return all(self.__eq__(a) for a in asarray.flat)
    
        # Short-circuit exact equality.
        if actual == self.expected:
            return True
    
        # If either type is non-numeric, fall back to strict equality.
        # NB: we need Complex, rather than just Number, to ensure that __abs__,
        # __sub__, and __float__ are defined.
        if not (
            isinstance(self.expected, (Complex, Decimal))
            and isinstance(actual, (Complex, Decimal))
        ):
            return False
    
        # Allow the user to control whether NaNs are considered equal to each
        # other or not.  The abs() calls are for compatibility with complex
        # numbers.
        if math.isnan(abs(self.expected)):
            return self.nan_ok and math.isnan(abs(actual))
    
        # Infinity shouldn't be approximately equal to anything but itself, but
        # if there's a relative tolerance, it will be infinite and infinity
        # will seem approximately equal to everything.  The equal-to-itself
        # case would have been short circuited above, so here we can just
        # return false if the expected value is infinite.  The abs() call is
        # for compatibility with complex numbers.
        if math.isinf(abs(self.expected)):
            return False
    
        # Return true if the two numbers are within the tolerance.
>       result: bool = abs(self.expected - actual) <= self.tolerance
E       TypeError: unsupported operand type(s) for -: 'float' and 'decimal.Decimal'

/data/pydeps/marta/_pytest/python_api.py:459: TypeError
_______________________________ test_error_case ________________________________

    def test_error_case():
        start = date(2007, 10, 31)
        asof = date(2008, 11, 30)
        end = date(2008, 11, 30)
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_german_0.py:21: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_german_0.py::test_specific_date_adjustment
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_dcc_dcfc_30_360_german_0.py::test_error_case
============================== 2 failed in 0.12s ===============================
"""