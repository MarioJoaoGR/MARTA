
import pytest
from pytutils.mappings import ProcessLocal
import os

def test_invalid_inputs():
    plocal = ProcessLocal()
    with pytest.raises(KeyError):
        plocal['test']  # Initially, the mapping should be empty and raise KeyError
        
    plocal['test'] = True
    initial_value = plocal['test']
    assert initial_value is True
    
    new_pid = os.getpid() + 1  # Simulate a different PID
    with pytest.raises(KeyError):
        plocal._handle_pid(new_pid=lambda: new_pid)  # Using a lambda to pass the simulated PID
        
    with pytest.raises(KeyError):
        plocal['test']  # After wiping, the mapping should be empty again and raise KeyError

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProcessLocal__handle_pid_0_test_invalid_inputs.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal__handle_pid_0_test_invalid_inputs.py:3: in <module>
    from pytutils.mappings import ProcessLocal
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal__handle_pid_0_test_invalid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""