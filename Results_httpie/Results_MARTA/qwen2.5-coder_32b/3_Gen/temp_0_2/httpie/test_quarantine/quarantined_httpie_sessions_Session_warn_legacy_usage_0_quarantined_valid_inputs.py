
import pytest
from httpie.sessions import Session
from pathlib import Path
from httpie.sessions import Environment
from unittest.mock import patch, MagicMock

@pytest.fixture(params=[False, True])
def valid_session(request):
    env = Environment()
    session = Session(
        path=Path('test_session.json'),
        env=env,
        bound_host='example.com',
        session_id='unique_id'
    )
    yield session
    # Clean up after the test if necessary

def test_valid_inputs(valid_session, suppress_legacy_warnings):
    with patch('httpie.sessions.Environment.log_error') as mock_log_error:
        valid_session.suppress_legacy_warnings = suppress_legacy_warnings
        warning_message = "This is a legacy usage warning."
        valid_session.warn_legacy_usage(warning_message)
        
        if suppress_legacy_warnings:
            mock_log_error.assert_not_called()
        else:
            mock_log_error.assert_called_once_with(warning_message, level='WARNING')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_Session_warn_legacy_usage_0_test_valid_inputs.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
__________________ ERROR at setup of test_valid_inputs[False] __________________
file /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_Session_warn_legacy_usage_0_test_valid_inputs.py, line 20
  def test_valid_inputs(valid_session, suppress_legacy_warnings):
E       fixture 'suppress_legacy_warnings' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, valid_session
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_Session_warn_legacy_usage_0_test_valid_inputs.py:20
__________________ ERROR at setup of test_valid_inputs[True] ___________________
file /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_Session_warn_legacy_usage_0_test_valid_inputs.py, line 20
  def test_valid_inputs(valid_session, suppress_legacy_warnings):
E       fixture 'suppress_legacy_warnings' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, valid_session
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_Session_warn_legacy_usage_0_test_valid_inputs.py:20
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_Session_warn_legacy_usage_0_test_valid_inputs.py::test_valid_inputs[False]
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_sessions_Session_warn_legacy_usage_0_test_valid_inputs.py::test_valid_inputs[True]
============================== 2 errors in 0.27s ===============================
"""