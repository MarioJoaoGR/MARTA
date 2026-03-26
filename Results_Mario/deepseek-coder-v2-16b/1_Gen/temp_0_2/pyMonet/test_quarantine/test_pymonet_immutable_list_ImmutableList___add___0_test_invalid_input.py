
from pymonet import ImmutableList

def test_invalid_input():
    # Test adding an invalid type to ImmutableList
    list1 = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    
    try:
        result = list1.__add__("invalid input")  # This should raise a ValueError
        assert False, "Expected ValueError but got no exception"
    except ValueError as e:
        assert str(e) == 'ImmutableList: you can not add any other instace than ImmutableList', f"Unexpected error message: {str(e)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___add___0_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___add___0_test_invalid_input.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""