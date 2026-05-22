
import unittest
from unittest.mock import patch
from httpie.utils import is_expired

class TestHttpieUtilsIsExpired(unittest.TestCase):
    @patch('httpie.utils.now', return_value=1672502400.0)  # Example current time, you can adjust this as needed
    def test_valid_input(self, mock_now):
        now = mock_now()  # Capture the mocked value for comparison
        
        # Test when expires is None
        self.assertFalse(is_expired(None))
        
        # Test when expires is in the past
        self.assertTrue(is_expired(now - 3600))  # One hour before now
        
        # Test when expires is equal to current time
        self.assertTrue(is_expired(now))
        
        # Test when expires is in the future
        self.assertFalse(is_expired(now + 3600))  # One hour after now

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_utils_is_expired_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_is_expired_0_test_valid_input.py:4:0: E0611: No name 'is_expired' in module 'httpie.utils' (no-name-in-module)


"""