
# Module: pytutils.enum
import pytest
from pytutils.enum import LookupEnumMixin
import enum

class MyEnum(LookupEnumMixin, metaclass=enum.EnumMeta):
    A = 1
    B = 2

    lookup_by_name = {
        'A': 1,
        'B': 2
    }
    lookup_by_value = {
        1: 'A',
        2: 'B'
    }

class AnotherEnum(LookupEnumMixin, metaclass=enum.EnumMeta):
    X = 10
    Y = 20

    lookup_by_name = {
        'X': 10,
        'Y': 20
    }
    lookup_by_value = {
        10: 'X',
        20: 'Y'
    }

def test_lookup_by_any_custom_enum():
    result = MyEnum.lookup_by_any()
    expected = {'A': 1, 'B': 2, 1: 'A', 2: 'B'}
    assert result == expected, f"Expected {expected}, but got {result}"

def test_lookup_by_any_builtin_enum():
    class MyEnum(LookupEnumMixin, metaclass=enum.EnumMeta):
        A = 1
        B = 2

        lookup_by_name = {
            'A': 1,
            'B': 2
        }
        lookup_by_value = {
            1: 'A',
            2: 'B'
        }
    result = MyEnum.lookup_by_any()
    expected = {'A': 1, 'B': 2, 1: 'A', 2: 'B'}
    assert result == expected, f"Expected {expected}, but got {result}"

def test_lookup_by_any_another_enum():
    result = AnotherEnum.lookup_by_any()
    expected = {'X': 10, 'Y': 20, 10: 'X', 20: 'Y'}
    assert result == expected, f"Expected {expected}, but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_any_0
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_any_0.py:34:13: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_any_0.py:51:13: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_any_0.py:56:13: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)


"""