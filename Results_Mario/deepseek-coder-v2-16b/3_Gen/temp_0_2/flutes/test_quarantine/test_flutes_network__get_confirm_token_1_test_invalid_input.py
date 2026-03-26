
import pytest
from unittest.mock import MagicMock
from flutes.network import _get_confirm_token

def test_invalid_input():
    # Create a mock response with cookies
    resp = MagicMock()
    resp.cookies = {
        'download_warning1': 'value1',
        'not_download_warning': 'value2'
    }
    
    # Call the function with the mock response
    token = _get_confirm_token(resp)
    
    # Assert that the returned value is None since we are looking for a key starting with 'download_warning'
    assert token is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_network__get_confirm_token_1_test_invalid_input
flutes/Test4DT_tests/test_flutes_network__get_confirm_token_1_test_invalid_input.py:4:0: E0611: No name '_get_confirm_token' in module 'flutes.network' (no-name-in-module)


"""