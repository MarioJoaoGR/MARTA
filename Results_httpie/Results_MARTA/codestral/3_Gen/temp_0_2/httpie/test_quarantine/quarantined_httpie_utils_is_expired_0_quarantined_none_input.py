
import unittest
from unittest.mock import patch
from httpie.utils import is_expired

class TestIsExpired(unittest.TestCase):
    @patch('httpie.utils.is_expired')  # Mock the function to isolate the test
    def test_none_input(self, mock_is_expired):
        # Call the function with None as input
        result = is_expired(None)
        
        # Assert that the function returns False when expires is None
        self.assertFalse(result)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_utils_is_expired_0_test_none_input
httpie/Test4DT_tests_codestral/test_httpie_utils_is_expired_0_test_none_input.py:4:0: E0611: No name 'is_expired' in module 'httpie.utils' (no-name-in-module)


"""