
import pytest
from unittest.mock import patch, MagicMock
from httpie.internal.update_warnings import _get_suppress_context
from contextlib import nullcontext, suppress

@pytest.fixture(autouse=True)
def mock_environment():
    with patch('httpie.internal.update_warnings._get_suppress_context') as mock_func:
        yield mock_func

def test_get_suppress_context_with_developer_mode_enabled(mock_environment):
    env = MagicMock()
    env.config.developer_mode = True
    mock_environment.return_value = nullcontext()
    
    ctx_mgr = _get_suppress_context(env)
    with ctx_mgr:
        raise ValueError("Test Error")  # This should not be suppressed

def test_get_suppress_context_with_developer_mode_disabled(mock_environment):
    env = MagicMock()
    env.config.developer_mode = False
    mock_environment.return_value = suppress(BaseException)
    
    ctx_mgr = _get_suppress_context(env)
    with ctx_mgr:
        raise ValueError("Test Error")  # This should be suppressed

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

httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings__get_suppress_context_0_test_edge_cases.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
____________ test_get_suppress_context_with_developer_mode_enabled _____________

mock_environment = <MagicMock name='_get_suppress_context' id='139741817899664'>

    def test_get_suppress_context_with_developer_mode_enabled(mock_environment):
        env = MagicMock()
        env.config.developer_mode = True
        mock_environment.return_value = nullcontext()
    
        ctx_mgr = _get_suppress_context(env)
        with ctx_mgr:
>           raise ValueError("Test Error")  # This should not be suppressed
E           ValueError: Test Error

httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings__get_suppress_context_0_test_edge_cases.py:19: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings__get_suppress_context_0_test_edge_cases.py::test_get_suppress_context_with_developer_mode_enabled
========================= 1 failed, 1 passed in 0.21s ==========================
"""