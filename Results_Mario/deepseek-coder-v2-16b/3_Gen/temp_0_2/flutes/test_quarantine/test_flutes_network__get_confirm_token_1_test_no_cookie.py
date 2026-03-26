
import pytest
from flutes.network import _get_confirm_token
import requests

@pytest.mark.parametrize("resp", [requests.Response()])
def test_no_cookie(resp):
    # Mocking a response with cookies for testing
    resp.cookies['download_warning_123'] = 'test_value'
    resp.cookies['other_key'] = 'other_value'
    
    token = _get_confirm_token(resp)
    assert token == 'test_value'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_network__get_confirm_token_1_test_no_cookie
flutes/Test4DT_tests/test_flutes_network__get_confirm_token_1_test_no_cookie.py:3:0: E0611: No name '_get_confirm_token' in module 'flutes.network' (no-name-in-module)


"""