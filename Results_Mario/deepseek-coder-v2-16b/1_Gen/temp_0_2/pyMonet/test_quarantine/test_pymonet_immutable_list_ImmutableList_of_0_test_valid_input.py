
from pymonet import ImmutableList

def test_valid_input():
    # Creating an immutable list with elements 1, 2, 3
    my_list = ImmutableList.of(1, 2, 3)
    
    # Checking if the list is created correctly
    assert my_list.head == 1
    assert my_list.tail.head == 2
    assert my_list.tail.tail.head == 3
    assert my_list.tail.tail.tail.is_empty is True
    
    # Trying to mutate the list will raise an error (since it's immutable)
    try:
        my_list.head = 4
        assert False, "Expected TypeError but got no exception"
    except TypeError as e:
        assert str(e) == "ImmutableList object does not support item assignment", f"Unexpected error message: {str(e)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList_of_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList_of_0_test_valid_input.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""