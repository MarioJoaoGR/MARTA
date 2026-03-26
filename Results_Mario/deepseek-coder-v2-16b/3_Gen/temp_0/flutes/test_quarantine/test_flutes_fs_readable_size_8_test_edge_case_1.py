
import pytest

def test_edge_case_1():
    """Test edge case with None input for size"""
    with pytest.raises(TypeError):
        readable_size(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_fs_readable_size_8_test_edge_case_1
flutes/Test4DT_tests/test_flutes_fs_readable_size_8_test_edge_case_1.py:7:8: E0602: Undefined variable 'readable_size' (undefined-variable)

"""