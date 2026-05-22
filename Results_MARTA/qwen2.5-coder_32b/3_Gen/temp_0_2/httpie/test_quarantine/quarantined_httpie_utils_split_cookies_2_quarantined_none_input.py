
import pytest
from httpie.utils import split_cookies
from unittest.mock import patch

def test_split_cookies_none():
    with patch('httpie.utils.RE_COOKIE_SPLIT', create=True) as mock_re:
        mock_re.return_value = lambda x: [] if not x else [x]
        assert split_cookies(None) == []

def test_split_cookies_empty():
    with patch('httpie.utils.RE_COOKIE_SPLIT', create=True) as mock_re:
        mock_re.return_value = lambda x: [] if not x else [x]
        assert split_cookies('') == []

def test_split_cookies_valid():
    with patch('httpie.utils.RE_COOKIE_SPLIT', create=True) as mock_re:
        mock_re.return_value = lambda x: [x] if x else []
        assert split_cookies('cookie1=value1, cookie2=value2') == ['cookie1=value1', 'cookie2=value2']

def test_split_cookies_valid_with_domain():
    with patch('httpie.utils.RE_COOKIE_SPLIT', create=True) as mock_re:
        mock_re.return_value = lambda x: [x] if x else []
        assert split_cookies('; path=/; domain=.example.com; Secure') == ['; path=/; domain=.example.com; Secure']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_split_cookies_2_test_none_input.py . [ 25%]
.FF                                                                      [100%]

=================================== FAILURES ===================================
___________________________ test_split_cookies_valid ___________________________

    def test_split_cookies_valid():
        with patch('httpie.utils.RE_COOKIE_SPLIT', create=True) as mock_re:
            mock_re.return_value = lambda x: [x] if x else []
>           assert split_cookies('cookie1=value1, cookie2=value2') == ['cookie1=value1', 'cookie2=value2']
E           AssertionError: assert <MagicMock na...639182513936'> == ['cookie1=val...okie2=value2']
E             
E             Use -v to get more diff

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_split_cookies_2_test_none_input.py:19: AssertionError
_____________________ test_split_cookies_valid_with_domain _____________________

    def test_split_cookies_valid_with_domain():
        with patch('httpie.utils.RE_COOKIE_SPLIT', create=True) as mock_re:
            mock_re.return_value = lambda x: [x] if x else []
>           assert split_cookies('; path=/; domain=.example.com; Secure') == ['; path=/; domain=.example.com; Secure']
E           AssertionError: assert <MagicMock na...639190247120'> == ['; path=/; d....com; Secure']
E             
E             Use -v to get more diff

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_split_cookies_2_test_none_input.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_split_cookies_2_test_none_input.py::test_split_cookies_valid
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_split_cookies_2_test_none_input.py::test_split_cookies_valid_with_domain
========================= 2 failed, 2 passed in 0.17s ==========================
"""