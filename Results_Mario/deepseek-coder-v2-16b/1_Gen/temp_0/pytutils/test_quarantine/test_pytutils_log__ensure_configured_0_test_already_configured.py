
import pytest
from pytutils.log import _ensure_configured, configure

# Define a fixture to provide a mock for _CONFIGURED
@pytest.fixture(autouse=True)
def setup_mock_config():
    # Create a mutable default value for _CONFIGURED
    global _CONFIGURED
    _CONFIGURED = []

def test_already_configured():
    # Initially, _CONFIGURED should be empty
    assert not _CONFIGURED
    
    # Call the function with no parameters to ensure configuration
    _ensure_configured()
    
    # After calling the function, _CONFIGURED should have a True value
    assert len(_CONFIGURED) == 1 and _CONFIGURED[0] is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_log__ensure_configured_0_test_already_configured.py F [100%]

=================================== FAILURES ===================================
___________________________ test_already_configured ____________________________

    def test_already_configured():
        # Initially, _CONFIGURED should be empty
        assert not _CONFIGURED
    
        # Call the function with no parameters to ensure configuration
        _ensure_configured()
    
        # After calling the function, _CONFIGURED should have a True value
>       assert len(_CONFIGURED) == 1 and _CONFIGURED[0] is True
E       assert (0 == 1)
E        +  where 0 = len([])

pytutils/Test4DT_tests/test_pytutils_log__ensure_configured_0_test_already_configured.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log__ensure_configured_0_test_already_configured.py::test_already_configured
============================== 1 failed in 0.06s ===============================
"""