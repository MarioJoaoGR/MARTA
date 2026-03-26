
from pytutils.tlds import join_dom

def test_edge_case_none():
    # Test when both inputs are None
    assert join_dom(None, None) == None
    
    # Test when the first input is None
    assert join_dom(None, 'example') == 'example'
    
    # Test when the second input is None
    assert join_dom('com', None) == 'com'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_tlds_join_dom_0_test_edge_case_none
pytutils/Test4DT_tests/test_pytutils_tlds_join_dom_0_test_edge_case_none.py:2:0: E0611: No name 'join_dom' in module 'pytutils.tlds' (no-name-in-module)


"""