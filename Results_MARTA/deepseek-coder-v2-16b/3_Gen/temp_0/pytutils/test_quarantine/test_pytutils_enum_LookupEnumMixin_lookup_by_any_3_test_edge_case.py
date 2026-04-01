
import pytest
from pytutils.enum import EnumMeta

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

def test_edge_case():
    assert ExampleEnum.lookup_by_any() == {'A': 1, 'B': 2, 1: 'A', 2: 'B'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_any_3_test_edge_case
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_any_3_test_edge_case.py:3:0: E0611: No name 'EnumMeta' in module 'pytutils.enum' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_any_3_test_edge_case.py:5:18: E0602: Undefined variable 'LookupEnumMixin' (undefined-variable)


"""