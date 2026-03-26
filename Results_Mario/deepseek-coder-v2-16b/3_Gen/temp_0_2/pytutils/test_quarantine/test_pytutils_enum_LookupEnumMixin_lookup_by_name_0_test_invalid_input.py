
import pytest
from pytutils.enum import LookupEnumMixin

# Define an invalid type for testing
class InvalidType:
    pass

def test_invalid_input():
    with pytest.raises(AttributeError):
        InvalidType.lookup_by_name()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_name_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_0_test_invalid_input.py:11:8: E1101: Class 'InvalidType' has no 'lookup_by_name' member (no-member)


"""