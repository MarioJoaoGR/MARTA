
import pytest
from flutes.network import _get_confirm_token
from unittest.mock import Mock

@pytest.mark.parametrize("cookies, expected", [
    ({'download_warning': 'token123'}, 'token123'),
    ({'not_download_warning': 'other_token'}, None),
    ({}, None)
])
def test_get_confirm_token(cookies, expected):
    mock_resp = Mock()
    mock_resp.cookies = cookies
    assert _get_confirm_token(mock_resp) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_network__get_confirm_token_0_test_no_cookie
flutes/Test4DT_tests/test_flutes_network__get_confirm_token_0_test_no_cookie.py:3:0: E0611: No name '_get_confirm_token' in module 'flutes.network' (no-name-in-module)


"""