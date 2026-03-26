
import pytest
from pytutils.enum import LookupEnumMixin

# Define a sample enum for testing
@pytest.mark.parametrize("cls", [LookupEnumMixin])
def test_valid_input(cls):
    class Color(metaclass=LookupEnumMixin, Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    expected_lookup = {
        1: Color.RED,
        2: Color.GREEN,
        3: Color.BLUE
    }
    
    assert cls.lookup_by_value(Color) == expected_lookup

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_value_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_value_0_test_valid_input.py:8:48: E0001: Parsing failed: 'positional argument follows keyword argument (Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_value_0_test_valid_input, line 8)' (syntax-error)


"""