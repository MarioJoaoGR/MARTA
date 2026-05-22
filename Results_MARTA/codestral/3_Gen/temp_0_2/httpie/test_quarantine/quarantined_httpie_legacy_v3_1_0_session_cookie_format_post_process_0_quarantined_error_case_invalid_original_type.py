
import pytest
from unittest.mock import patch
from httpie.legacy.v3_1_0_session_cookie_format import post_process
from typing import List, Dict, Any, Type

def test_error_case_invalid_original_type():
    with patch('builtins.isinstance', side_effect=TypeError):
        normalized_cookies = [{'name': 'cookie1', 'value': 'value1'}, {'name': 'cookie2', 'value': 'value2'}]
        original_type = list  # Using a type that is not a subclass of dict for the test
        
        with pytest.raises(TypeError):
            post_process(normalized_cookies, original_type=original_type)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_legacy_v3_1_0_session_cookie_format_post_process_0_test_error_case_invalid_original_type.py F [100%]

=================================== FAILURES ===================================
____________________ test_error_case_invalid_original_type _____________________

    def test_error_case_invalid_original_type():
        with patch('builtins.isinstance', side_effect=TypeError):
            normalized_cookies = [{'name': 'cookie1', 'value': 'value1'}, {'name': 'cookie2', 'value': 'value2'}]
            original_type = list  # Using a type that is not a subclass of dict for the test
    
>           with pytest.raises(TypeError):

httpie/Test4DT_tests_codestral/test_httpie_legacy_v3_1_0_session_cookie_format_post_process_0_test_error_case_invalid_original_type.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1137: in _increment_mock_call
    _call = _Call((args, kwargs), two=True)
/usr/local/lib/python3.11/unittest/mock.py:2495: in __new__
    if isinstance(first, str):
/usr/local/lib/python3.11/unittest/mock.py:1123: in __call__
    self._increment_mock_call(*args, **kwargs)
/usr/local/lib/python3.11/unittest/mock.py:1131: in _increment_mock_call
    self.called = True
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='isinstance' id='139992752855696'>, name = 'called'
value = True

    def __setattr__(self, name, value):
        if name in _allowed_names:
            # property setters go through here
>           return object.__setattr__(self, name, value)
E           RecursionError: maximum recursion depth exceeded

/usr/local/lib/python3.11/unittest/mock.py:765: RecursionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_legacy_v3_1_0_session_cookie_format_post_process_0_test_error_case_invalid_original_type.py::test_error_case_invalid_original_type
============================== 1 failed in 6.63s ===============================
"""