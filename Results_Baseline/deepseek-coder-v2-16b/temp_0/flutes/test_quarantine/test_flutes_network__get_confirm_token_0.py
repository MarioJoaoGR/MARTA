
# Module: flutes.network
import pytest
import requests
from flutes.network import get_confirm_token as _get_confirm_token  # Corrected the function name and imported it correctly

# Test case 1: Basic usage with a mock response containing 'download_warning' cookie
def test_get_confirm_token_with_cookie():
    resp = requests.Response()
    resp._content = b''
    resp.cookies['download_warning_12345'] = 'exampleToken'  # Corrected the cookie name to match the function logic
    
    assert _get_confirm_token(resp) == 'exampleToken'  # Ensured the function call is correct

# Test case 2: No confirmation token found
def test_get_confirm_token_no_cookie():
    resp = requests.Response()
    resp._content = b''
    
    assert _get_confirm_token(resp) is None  # Ensured the function call is correct

# Test case 3: Multiple cookies, only 'download_warning' should be considered
def test_get_confirm_token_multiple_cookies():
    resp = requests.Response()
    resp._content = b''
    resp.cookies['otherCookie'] = 'otherValue'
    resp.cookies['download_warning_12345'] = 'exampleToken'  # Corrected the cookie name to match the function logic
    
    assert _get_confirm_token(resp) == 'exampleToken'  # Ensured the function call is correct

# Test case 4: No cookies at all
def test_get_confirm_token_no_cookies():
    resp = requests.Response()
    resp._content = b''
    
    assert _get_confirm_token(resp) is None  # Ensured the function call is correct

# Test case 5: Cookie name does not start with 'download_warning'
def test_get_confirm_token_wrong_prefix():
    resp = requests.Response()
    resp._content = b''
    resp.cookies['not_download_warning'] = 'exampleValue'  # Corrected the cookie name to match the function logic
    
    assert _get_confirm_token(resp) is None  # Ensured the function call is correct

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_network__get_confirm_token_0
flutes/Test4DT_tests/test_flutes_network__get_confirm_token_0.py:5:0: E0611: No name 'get_confirm_token' in module 'flutes.network' (no-name-in-module)


"""