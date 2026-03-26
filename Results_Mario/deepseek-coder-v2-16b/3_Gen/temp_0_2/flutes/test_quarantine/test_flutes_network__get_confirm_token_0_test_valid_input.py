
import pytest
from unittest.mock import MagicMock
from flutes.network import _get_confirm_token

def test_valid_input():
    # Create a mock HTTP response object with cookies
    resp = MagicMock()
    resp.cookies = {
        'download_warning_123': 'value1',
        'other_cookie': 'value2'
    }
    
    # Call the function under test
    token = _get_confirm_token(resp)
    
    # Assert that the correct token is returned
    assert token == 'value1'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_network__get_confirm_token_0_test_valid_input
flutes/Test4DT_tests/test_flutes_network__get_confirm_token_0_test_valid_input.py:4:0: E0611: No name '_get_confirm_token' in module 'flutes.network' (no-name-in-module)


"""