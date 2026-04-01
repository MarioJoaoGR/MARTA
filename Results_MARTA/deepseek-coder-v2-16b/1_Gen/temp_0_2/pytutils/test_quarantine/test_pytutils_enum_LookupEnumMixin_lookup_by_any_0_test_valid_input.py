
import pytest
from pytutils.enum import LookupEnumMixin

# Assuming IntEnum is defined in a module or imported correctly
class MyEnum(LookupEnumMixin):
    lookup_by_name = {1: 'one', 2: 'two'}
    lookup_by_value = {0: 'zero', 1: 'one'}

def test_valid_input():
    combined_lookup = MyEnum.lookup_by_any()
    assert combined_lookup == {'one': 1, 'two': 2, 'zero': 0}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_any_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_any_0_test_valid_input.py:11:22: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)


"""