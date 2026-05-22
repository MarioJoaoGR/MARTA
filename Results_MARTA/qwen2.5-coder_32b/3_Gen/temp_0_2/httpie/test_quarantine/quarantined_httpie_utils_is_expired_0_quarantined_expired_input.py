
import pytest
from unittest.mock import patch
from httpie.utils import is_expired

def test_is_expired():
    # Test when expires is None
    assert not is_expired(None)
    
    # Test when expires is in the past
    with patch('httpie.utils.now', return_value=100):  # Mocking now to be a fixed value for testing
        assert is_expired(90)  # Should return True as it's expired (before current time)
    
    # Test when expires is in the future
    with patch('httpie.utils.now', return_value=100):
        assert not is_expired(110)  # Should return False as it's not yet expired

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_utils_is_expired_0_test_expired_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_is_expired_0_test_expired_input.py:4:0: E0611: No name 'is_expired' in module 'httpie.utils' (no-name-in-module)


"""