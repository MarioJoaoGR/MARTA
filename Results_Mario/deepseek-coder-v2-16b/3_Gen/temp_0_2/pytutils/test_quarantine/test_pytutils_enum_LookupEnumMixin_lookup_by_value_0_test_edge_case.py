
import pytest
from pytutils.enum import LookupEnumMixin

@pytest.mark.parametrize("cls", [Color])
def test_lookup_by_value(cls):
    # Assuming Color is an Enum class defined somewhere in your module
    from enum import Enum
    
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    expected_output = {1: Color.RED, 2: Color.GREEN, 3: Color.BLUE}
    assert LookupEnumMixin().lookup_by_value(cls) == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_value_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_value_0_test_edge_case.py:5:33: E0602: Undefined variable 'Color' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_value_0_test_edge_case.py:16:11: E1121: Too many positional arguments for method call (too-many-function-args)


"""