
import pytest
from pytutils.enum import LookupEnumMixin

@pytest.mark.parametrize("cls", [MyEnum])
def test_lookup_by_any(cls):
    class MyEnum(LookupEnumMixin, int):
        lookup_by_name = {1: 'one', 2: 'two'}
        lookup_by_value = {0: 'zero', 1: 'one'}
    
    combined_lookup = LookupEnumMixin.lookup_by_any(cls)
    assert combined_lookup == {'one': 1, 'two': 2, 'zero': 0}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_any_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_any_0_test_edge_case.py:5:33: E0602: Undefined variable 'MyEnum' (undefined-variable)


"""