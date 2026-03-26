
import pytest
from pytutils.path import join_each

def test_edge_case_empty_list():
    directory_path = '/home/user'
    file_names = []
    
    with pytest.raises(StopIteration):
        for _ in join_each(directory_path, file_names:
            pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_path_join_each_2_test_edge_case_empty_list
pytutils/Test4DT_tests/test_pytutils_path_join_each_2_test_edge_case_empty_list.py:10:54: E0001: Parsing failed: 'invalid syntax (Test4DT_tests.test_pytutils_path_join_each_2_test_edge_case_empty_list, line 10)' (syntax-error)


"""