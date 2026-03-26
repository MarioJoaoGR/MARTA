
import pytest
from pytutils.enum import LookupEnumMixin
from enum import Enum

def test_invalid_input():
    class InvalidEnum(LookupEnumMixin):
        pass
    
    with pytest.raises(TypeError):
        InvalidEnum.lookup_by_name()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_name_1_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_1_test_invalid_input.py:11:8: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)


"""