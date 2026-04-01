
import pytest
from pytutils.enum import LookupEnumMixin

def test_invalid_input():
    class Colors(LookupEnumMixin, metaclass=type):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    with pytest.raises(TypeError):
        # Attempt to call lookup_by_name without providing an enum class instance
        LookupEnumMixin.lookup_by_name()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_name_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_0_test_invalid_input.py:13:8: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)


"""