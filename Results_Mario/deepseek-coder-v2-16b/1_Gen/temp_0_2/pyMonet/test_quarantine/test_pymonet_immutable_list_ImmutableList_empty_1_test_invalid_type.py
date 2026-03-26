
from pymonet import ImmutableList

def test_invalid_type():
    # Attempt to create an instance of ImmutableList with a non-empty list should raise a TypeError
    try:
        my_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
        assert False, "Expected TypeError but no error was raised"
    except TypeError as e:
        # Expected error due to invalid type usage
        assert str(e) == "Cannot create ImmutableList with both head and is_empty set", f"Unexpected error message: {str(e)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_empty_1_test_invalid_type
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_empty_1_test_invalid_type.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""