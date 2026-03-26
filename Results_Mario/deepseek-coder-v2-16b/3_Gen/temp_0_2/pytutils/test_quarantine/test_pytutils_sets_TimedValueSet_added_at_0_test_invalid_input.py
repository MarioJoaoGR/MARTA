
import pytest
from timed_value_set import TimedValueSet
import time

def test_invalid_input():
    tvs = TimedValueSet()
    
    # Test with no value set
    with pytest.raises(AttributeError):
        tvs.added_at()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_sets_TimedValueSet_added_at_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_invalid_input.py:3:0: E0401: Unable to import 'timed_value_set' (import-error)


"""