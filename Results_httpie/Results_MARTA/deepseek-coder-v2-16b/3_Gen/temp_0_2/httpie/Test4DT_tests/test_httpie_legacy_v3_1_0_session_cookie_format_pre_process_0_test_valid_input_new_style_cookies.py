
import pytest
from unittest.mock import patch, MagicMock
from httpie.legacy.v3_1_0_session_cookie_format import pre_process
from typing import List, Dict, Any

@pytest.fixture(autouse=True)
def mock_session():
    session = MagicMock()
    session.bound_host = "example.com"
    session.session_id = "12345"
    session.is_anonymous = False
    return session

@pytest.fixture(autouse=True)
def mock_cookies():
    return [{"name": "cookie3", "value": "value3"}, {"name": "cookie4", "value": "value4"}]

@patch('httpie.legacy.v3_1_0_session_cookie_format.INSECURE_COOKIE_JAR_WARNING', "{hostname} {session_id}")
@patch('httpie.legacy.v3_1_0_session_cookie_format.INSECURE_COOKIE_JAR_WARNING_FOR_NAMED_SESSIONS', " Additional warning for named sessions.")
@patch('httpie.legacy.v3_1_0_session_cookie_format.INSECURE_COOKIE_SECURITY_LINK', " Learn more at [link]")
def test_valid_input_new_style_cookies(mock_session, mock_cookies):
    result = pre_process(mock_session, mock_cookies)
    assert isinstance(result, list)
    assert len(result) == 2
    for cookie in result:
        assert 'name' in cookie
        assert 'value' in cookie
