
# Module: pytutils.enum
# test_pytutils_enum.py
from enum import Enum
import pytest
from pytutils.enum import LookupEnumMixin

class Color(LookupEnumMixin, Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class ExampleEnum(LookupEnumMixin, Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3

def test_lookup_by_value_color():
    lookup_dict = Color.lookup_by_value()
    assert lookup_dict == {1: Color.RED, 2: Color.GREEN, 3: Color.BLUE}

def test_lookup_by_value_exampleenum():
    lookup_dict = ExampleEnum.lookup_by_value()
    assert lookup_dict == {1: ExampleEnum.FIRST, 2: ExampleEnum.SECOND, 3: ExampleEnum.THIRD}

def test_lookup_by_value_empty_enum():
    class EmptyEnum(LookupEnumMixin, Enum):
        EMPTY = 0
    
    lookup_dict = EmptyEnum.lookup_by_value()
    assert lookup_dict == {0: EmptyEnum.EMPTY}

def test_lookup_by_value_invalid_enum():
    class InvalidEnum(LookupEnumMixin, Enum):
        INVALID = "not a valid value"
    
    with pytest.raises(TypeError):
        InvalidEnum.lookup_by_value()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_value_0
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_value_0.py:19:18: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_value_0.py:23:18: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_value_0.py:30:18: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_value_0.py:38:8: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)


"""