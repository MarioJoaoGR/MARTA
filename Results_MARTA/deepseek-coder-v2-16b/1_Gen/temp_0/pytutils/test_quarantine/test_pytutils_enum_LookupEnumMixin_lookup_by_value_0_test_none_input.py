
from pytutils.enum import LookupEnumMixin
import pytest

def test_none_input():
    with pytest.raises(TypeError):
        LookupEnumMixin.lookup_by_value()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_value_0_test_none_input
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_value_0_test_none_input.py:7:8: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)


"""