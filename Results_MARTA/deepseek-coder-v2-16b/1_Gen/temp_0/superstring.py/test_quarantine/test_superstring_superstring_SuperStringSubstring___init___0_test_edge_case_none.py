
import pytest
from superstring.superstring import SuperStringSubstring

def test_edge_case_none():
    # Test when start_index and end_index are None
    ss = SuperStringSubstring("Hello, World!", None, None)
    with pytest.raises(ValueError):
        ss.get_substring()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringSubstring___init___0_test_edge_case_none
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring___init___0_test_edge_case_none.py:9:8: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)


"""