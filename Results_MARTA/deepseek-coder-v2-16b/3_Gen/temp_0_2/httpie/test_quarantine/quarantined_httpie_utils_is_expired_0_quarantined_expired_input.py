
import unittest
from unittest.mock import patch
from httpie.utils import is_expired

class TestHttpieUtilsIsExpired(unittest.TestCase):
    @patch('httpie.utils.now', return_value=1000.0)  # Mocking the current time to be 1000 seconds since epoch
    def test_expired_input(self, mock_time):
        # Test when expires is None
        self.assertFalse(is_expired(None))
        
        # Test when expires is earlier than or equal to now (mocked time)
        self.assertTrue(is_expired(900.0))  # 900 seconds before the mocked current time
        
        # Test when expires is later than now (mocked time)
        self.assertFalse(is_expired(1100.0))  # 1100 seconds after the mocked current time

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_utils_is_expired_0_test_expired_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_is_expired_0_test_expired_input.py:4:0: E0611: No name 'is_expired' in module 'httpie.utils' (no-name-in-module)


"""