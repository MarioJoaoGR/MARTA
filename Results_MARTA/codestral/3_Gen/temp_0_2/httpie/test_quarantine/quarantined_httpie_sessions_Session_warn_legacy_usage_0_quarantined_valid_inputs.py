
import pytest
from httpie.sessions import Session
from pathlib import Path
from httpie.sessions import Environment
from unittest.mock import patch

@pytest.fixture(scope="function")
def valid_session():
    env = Environment()
    yield Session(path=Path("test_session.json"), env=env, bound_host="example.com", session_id="unique_id")

@pytest.mark.parametrize("suppress_legacy_warnings", [False, True])
def test_valid_inputs(valid_session, suppress_legacy_warnings):
    with patch('httpie.sessions.Session.warn_legacy_usage'):
        session = valid_session
        assert isinstance(session, Session)
        assert session.suppress_legacy_warnings == suppress_legacy_warnings

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

httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_warn_legacy_usage_0_test_valid_inputs.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_valid_inputs[True] ____________________________

valid_session = {'headers': [], 'cookies': [], 'auth': {'type': None, 'username': None, 'password': None}}
suppress_legacy_warnings = True

    @pytest.mark.parametrize("suppress_legacy_warnings", [False, True])
    def test_valid_inputs(valid_session, suppress_legacy_warnings):
        with patch('httpie.sessions.Session.warn_legacy_usage'):
            session = valid_session
            assert isinstance(session, Session)
>           assert session.suppress_legacy_warnings == suppress_legacy_warnings
E           AssertionError: assert False == True
E            +  where False = {'headers': [], 'cookies': [], 'auth': {'type': None, 'username': None, 'password': None}}.suppress_legacy_warnings

httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_warn_legacy_usage_0_test_valid_inputs.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_sessions_Session_warn_legacy_usage_0_test_valid_inputs.py::test_valid_inputs[True]
========================= 1 failed, 1 passed in 0.15s ==========================
"""