
import pytest
from pathlib import Path
from httpie.sessions import Environment, get_httpie_session
from unittest.mock import patch

def test_invalid_inputs():
    env = Environment()
    config_dir = Path('path/to/config')
    
    # Test with invalid session name (not a string)
    with pytest.raises(TypeError):
        get_httpie_session(env, config_dir, 12345, None, 'http://example.com')
    
    # Test with empty session name
    with pytest.raises(ValueError):
        get_httpie_session(env, config_dir, '', None, 'http://example.com')

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

httpie/Test4DT_tests_codestral/test_httpie_sessions_get_httpie_session_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        env = Environment()
        config_dir = Path('path/to/config')
    
        # Test with invalid session name (not a string)
        with pytest.raises(TypeError):
            get_httpie_session(env, config_dir, 12345, None, 'http://example.com')
    
        # Test with empty session name
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

httpie/Test4DT_tests_codestral/test_httpie_sessions_get_httpie_session_0_test_invalid_inputs.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_sessions_get_httpie_session_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.24s ===============================
"""