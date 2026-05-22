
from httpie.cookies import HTTPieCookiePolicy
from unittest.mock import patch, MagicMock
import pytest

@patch('httpie.cookies.HTTPieCookiePolicy._is_local_host')
def test_return_ok_secure(mock_is_local_host, policy):
    mock_is_local_host.return_value = False

    request_https = MagicMock()
    request_https.scheme = 'https'
    request_https.hostname = 'example.com'

    request_http = MagicMock()
    request_http.scheme = 'http'
    request_http.hostname = 'localhost'

    policy_instance = HTTPieCookiePolicy()
    
    assert policy_instance.return_ok_secure('some_cookie', request_https) == True
    assert policy_instance.return_ok_secure('some_cookie', request_http) == False

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cookies_HTTPieCookiePolicy_return_ok_secure_0_test_valid_input_secure_host.py E [100%]

==================================== ERRORS ====================================
___________________ ERROR at setup of test_return_ok_secure ____________________
file /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cookies_HTTPieCookiePolicy_return_ok_secure_0_test_valid_input_secure_host.py, line 6
  @patch('httpie.cookies.HTTPieCookiePolicy._is_local_host')
  def test_return_ok_secure(mock_is_local_host, policy):
E       fixture 'policy' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cookies_HTTPieCookiePolicy_return_ok_secure_0_test_valid_input_secure_host.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cookies_HTTPieCookiePolicy_return_ok_secure_0_test_valid_input_secure_host.py::test_return_ok_secure
=============================== 1 error in 0.06s ===============================
"""