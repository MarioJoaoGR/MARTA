
import pytest
from pytutils.enum import LookupEnumMixin

@pytest.mark.parametrize("cls", [Colors])
def test_lookup_by_name(cls):
    class Colors(LookupEnumMixin, enum.Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    expected_output = {
        'RED': Colors.RED,
        'GREEN': Colors.GREEN,
        'BLUE': Colors.BLUE
    }
    
    assert LookupEnumMixin.lookup_by_name(cls) == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_name_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_0_test_edge_case.py:5:33: E0602: Undefined variable 'Colors' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_0_test_edge_case.py:7:34: E0602: Undefined variable 'enum' (undefined-variable)


"""