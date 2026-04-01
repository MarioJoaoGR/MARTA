
import pytest
from pytutils.mappings import ProcessLocal
import os

@pytest.fixture(autouse=True)
def setup_and_teardown():
    plocal = ProcessLocal()
    initial_pid = os.getpid()
    yield  # This is where the test runs
    new_pid = os.getpid()
    if initial_pid != new_pid:
        assert not hasattr(plocal, '__mapping'), "Mapping should have been wiped after PID change"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProcessLocal__handle_pid_0_test_valid_input.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal__handle_pid_0_test_valid_input.py:3: in <module>
    from pytutils.mappings import ProcessLocal
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal__handle_pid_0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""