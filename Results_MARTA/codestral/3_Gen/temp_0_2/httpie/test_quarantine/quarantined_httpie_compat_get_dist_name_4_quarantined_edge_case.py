
import unittest.mock as mock
from httpie.compat import get_dist_name

def test_get_dist_name():
    with mock.patch('httpie.compat.importlib_metadata') as mock_importlib_metadata:
        # Mock an EntryPoint object
        entry_point = mock.Mock()
        entry_point.value = 'some_module'
        
        # Mock the dist attribute of the EntryPoint
        dist = mock.Mock()
        dist.name = 'some_dist_name'
        entry_point.dist = dist
        
        # Call the function
        result = get_dist_name(entry_point)
        
        # Assertions
        assert result == 'some_dist_name'

# Example test case using pytest
def test_get_dist_name():
    with mock.patch('httpie.compat.importlib_metadata') as mock_importlib_metadata:
        entry_point = mock.Mock()
        entry_point.value = 'some_module'
        
        dist = mock.Mock()
        dist.name = 'some_dist_name'
        entry_point.dist = dist
        
        result = get_dist_name(entry_point)
        
        assert result == 'some_dist_name'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_compat_get_dist_name_4_test_edge_case
httpie/Test4DT_tests_codestral/test_httpie_compat_get_dist_name_4_test_edge_case.py:23:0: E0102: function already defined line 5 (function-redefined)


"""