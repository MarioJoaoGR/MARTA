
import pytest
from unittest.mock import patch
from httpie.sessions import remove_cookie_by_name

def test_remove_cookies(session):
    # Add cookies to the session
    session['cookies'] = [{'name': 'cookie1', 'domain': 'example.com', 'path': '/'}, {'name': 'cookie2', 'domain': 'example.com', 'path': '/'}]
    
    # Remove one of the cookies
    with patch('httpie.sessions.remove_cookie_by_name'):
        session.remove_cookies([{'name': 'cookie1'}])
        
        # Verify that remove_cookie_by_name was called for cookie1
        assert len(session['cookies']) == 1

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

httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_remove_cookies_0_test_edge_case.py E [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_remove_cookies _____________________
file /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_remove_cookies_0_test_edge_case.py, line 6
  def test_remove_cookies(session):
E       fixture 'session' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_remove_cookies_0_test_edge_case.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_remove_cookies_0_test_edge_case.py::test_remove_cookies
=============================== 1 error in 0.22s ===============================
"""