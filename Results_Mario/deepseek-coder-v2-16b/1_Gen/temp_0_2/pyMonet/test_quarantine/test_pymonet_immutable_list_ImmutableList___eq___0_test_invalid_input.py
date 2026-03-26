
from pymonet import ImmutableList

def test_invalid_input():
    # Test that invalid input raises a TypeError
    try:
        my_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
        mutated_list = my_list.tail.tail  # Attempt to mutate the list (which should raise a TypeError)
    except TypeError:
        assert True
    else:
        assert False, "Expected a TypeError but did not get one"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_immutable_list_ImmutableList___eq___0_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_immutable_list_ImmutableList___eq___0_test_invalid_input.py:2:0: E0611: No name 'ImmutableList' in module 'pymonet' (no-name-in-module)


"""