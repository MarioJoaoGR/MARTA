
# Module: pytutils.enum
# test_pytutils_enum.py
from enum import Enum
import pytest

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class CustomEnum(LookupEnumMixin, Enum):
    VALUE_ONE = 42
    VALUE_TWO = 100

# Test case for the lookup_by_name function with a predefined enumeration
def test_lookup_by_name_predefined():
    color_dict = LookupEnumMixin.lookup_by_name(Color)
    assert color_dict == {'RED': Color.RED, 'GREEN': Color.GREEN, 'BLUE': Color.BLUE}

# Test case for the lookup_by_name function with a custom enumeration
def test_lookup_by_name_custom():
    custom_dict = LookupEnumMixin.lookup_by_name(CustomEnum)
    assert custom_dict == {'VALUE_ONE': CustomEnum.VALUE_ONE, 'VALUE_TWO': CustomEnum.VALUE_TWO}

# Test case to ensure calling lookup_by_name on an instance raises a TypeError
def test_lookup_by_name_instance():
    with pytest.raises(TypeError):
        custom_instance = CustomEnum()
        custom_dict_from_instance = custom_instance.lookup_by_name()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_name_0
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_0.py:12:17: E0602: Undefined variable 'LookupEnumMixin' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_0.py:18:17: E0602: Undefined variable 'LookupEnumMixin' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_0.py:23:18: E0602: Undefined variable 'LookupEnumMixin' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_name_0.py:29:26: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)


"""