
import pytest
from unittest.mock import patch
from httpie.sessions import Session, Environment
from pathlib import Path

@pytest.fixture
def session():
    return Session(path=Path('session_file.json'), env=Environment(), bound_host='example.com', session_id='unique_id')

def test_warn_legacy_usage(session):
    with patch.object(Environment, 'log_error') as mock_log_error:
        warning = "This is a legacy usage warning."
        session.warn_legacy_usage(warning)
        
        # Check if the log_error method was called with the correct arguments
        mock_log_error.assert_called_once_with(warning, level='WARNING')
        
        # Ensure that suppress_legacy_warnings is set to True after the first call
        session.warn_legacy_usage(warning)  # Second call should not trigger log_error
        assert mock_log_error.call_count == 1

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_warn_legacy_usage_4_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
____________________________ test_warn_legacy_usage ____________________________

session = {'headers': [], 'cookies': [], 'auth': {'type': None, 'username': None, 'password': None}}

    def test_warn_legacy_usage(session):
        with patch.object(Environment, 'log_error') as mock_log_error:
            warning = "This is a legacy usage warning."
            session.warn_legacy_usage(warning)
    
            # Check if the log_error method was called with the correct arguments
>           mock_log_error.assert_called_once_with(warning, level='WARNING')

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_warn_legacy_usage_4_test_invalid_inputs.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:951: in assert_called_once_with
    return self.assert_called_with(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='log_error' id='140556972262992'>
args = ('This is a legacy usage warning.',), kwargs = {'level': 'WARNING'}
expected = call('This is a legacy usage warning.', level='WARNING')
actual = call('This is a legacy usage warning.', level=<LogLevel.WARNING: 'warning'>)
_error_message = <function NonCallableMock.assert_called_with.<locals>._error_message at 0x7fd5f863a480>
cause = None

    def assert_called_with(self, /, *args, **kwargs):
        """assert that the last call was made with the specified arguments.
    
        Raises an AssertionError if the args and keyword args passed in are
        different to the last call to the mock."""
        if self.call_args is None:
            expected = self._format_mock_call_signature(args, kwargs)
            actual = 'not called.'
            error_message = ('expected call not found.\nExpected: %s\n  Actual: %s'
                    % (expected, actual))
            raise AssertionError(error_message)
    
        def _error_message():
            msg = self._format_mock_failure_message(args, kwargs)
            return msg
        expected = self._call_matcher(_Call((args, kwargs), two=True))
        actual = self._call_matcher(self.call_args)
        if actual != expected:
            cause = expected if isinstance(expected, Exception) else None
>           raise AssertionError(_error_message()) from cause
E           AssertionError: expected call not found.
E           Expected: log_error('This is a legacy usage warning.', level='WARNING')
E             Actual: log_error('This is a legacy usage warning.', level=<LogLevel.WARNING: 'warning'>)

/usr/local/lib/python3.11/unittest/mock.py:939: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_Session_warn_legacy_usage_4_test_invalid_inputs.py::test_warn_legacy_usage
============================== 1 failed in 0.32s ===============================
"""