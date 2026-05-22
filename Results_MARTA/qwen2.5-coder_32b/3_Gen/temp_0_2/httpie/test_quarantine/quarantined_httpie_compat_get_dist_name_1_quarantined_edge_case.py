
import unittest.mock as mock
from httpie.compat import get_dist_name

def test_get_dist_name():
    with mock.patch('httpie.compat.importlib_metadata') as mock_importlib_metadata:
        # Mock an EntryPoint object
        entry_point = mock.Mock()
        dist = mock.Mock()
        dist.name = 'some_name'
        entry_point.dist = dist
        
        # Call the function
        result = get_dist_name(entry_point)
        
        # Assertions
        assert result == 'some_name'
        
        # Test when dist is None
        entry_point.dist = None
        result = get_dist_name(entry_point)
        assert result is None
        
        # Mock a PackageNotFoundError to test the exception handling
        mock_importlib_metadata.metadata.side_effect = importlib_metadata.PackageNotFoundError()
        result = get_dist_name(entry_point)
        assert result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_compat_get_dist_name_1_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_compat_get_dist_name_1_test_edge_case.py:25:55: E0602: Undefined variable 'importlib_metadata' (undefined-variable)


"""