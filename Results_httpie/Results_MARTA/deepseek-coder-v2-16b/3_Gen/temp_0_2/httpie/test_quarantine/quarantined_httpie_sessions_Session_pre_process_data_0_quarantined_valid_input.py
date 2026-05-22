
import pytest
from unittest.mock import patch
from httpie.sessions import Session
from httpie.sessions.legacy_headers import pre_process as legacy_headers_pre_process
from httpie.sessions.legacy_cookies import pre_process as legacy_cookies_pre_process
from typing import Dict, Any, List

@pytest.fixture
def valid_session():
    return Session(path='dummy', env=None, bound_host='example.com', session_id='12345')

def test_pre_process_data_with_headers(valid_session):
    data = {'headers': ['Header1: Value1', 'Header2: Value2'], 'cookies': []}
    with patch('httpie.sessions.legacy_headers.pre_process', side_effect=lambda self, values: [f'Processed {value}' for value in values]):
        result = valid_session.pre_process_data(data)
        assert result['headers'] == ['Processed Header1', 'Processed Header2']

def test_pre_process_data_with_cookies(valid_session):
    data = {'headers': [], 'cookies': ['cookie1=value1; cookie2=value2']}
    with patch('httpie.sessions.legacy_cookies.pre_process', side_effect=lambda self, values: [f'Processed {value}' for value in values]):
        result = valid_session.pre_process_data(data)
        assert result['cookies'] == ['Processed cookie1', 'Processed cookie2']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_sessions_Session_pre_process_data_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_pre_process_data_0_test_valid_input.py:5:0: E0401: Unable to import 'httpie.sessions.legacy_headers' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_pre_process_data_0_test_valid_input.py:6:0: E0401: Unable to import 'httpie.sessions.legacy_cookies' (import-error)


"""