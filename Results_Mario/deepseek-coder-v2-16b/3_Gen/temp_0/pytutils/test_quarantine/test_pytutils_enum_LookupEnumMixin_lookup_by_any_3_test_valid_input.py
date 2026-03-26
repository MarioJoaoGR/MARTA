
import pytest
from pytutils.enum import ExampleEnum

def test_valid_input():
    class ExampleEnum(LookupEnumMixin, metaclass=EnumMeta):
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

    result = ExampleEnum.lookup_by_any()
    expected = {'A': 1, 'B': 2, 1: 'A', 2: 'B'}
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_any_3_test_valid_input
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_any_3_test_valid_input.py:3:0: E0611: No name 'ExampleEnum' in module 'pytutils.enum' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_any_3_test_valid_input.py:6:22: E0602: Undefined variable 'LookupEnumMixin' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_any_3_test_valid_input.py:6:4: E0602: Undefined variable 'EnumMeta' (undefined-variable)


"""