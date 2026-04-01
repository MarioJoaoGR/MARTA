
import pytest
from unittest.mock import Mock
import requests
from flutes.network import _get_confirm_token

@pytest.fixture
def setup_response():
    resp = Mock(spec=requests.Response)
    resp.cookies = {
        'download_warning_cookie': 'some_value',
        'other_cookie': 'other_value'
    }
    return resp

def test_get_confirm_token_valid_input(setup_response):
    setup_response.cookies.__contains__.return_value = True
    assert _get_confirm_token(setup_response) == 'some_value'

def test_get_confirm_token_no_cookie():
    resp = Mock(spec=requests.Response)
    resp.cookies = {}
    assert _get_confirm_token(resp) is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_network__get_confirm_token_1_test_valid_input
flutes/Test4DT_tests/test_flutes_network__get_confirm_token_1_test_valid_input.py:5:0: E0611: No name '_get_confirm_token' in module 'flutes.network' (no-name-in-module)


"""