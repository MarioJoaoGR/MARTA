
import pytest
from pytutils.mappings import ProcessLocal
import os

def test_processlocal_wipes_mapping_on_pid_change():
    # Create an instance of ProcessLocal with a mock mapping factory that returns a dictionary
    plocal = ProcessLocal(mapping_factory=lambda: {})
    
    # Set a key in the ProcessLocal instance
    plocal['test'] = 'value'
    assert plocal['test'] == 'value', "Expected value to be set correctly"
    
    # Mock os.getpid to return a new PID, simulating a change
    original_pid = os.getpid()
    def mock_getpid():
        return original_pid + 1
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(os, 'getpid', mock_getpid)
        
        # After the PID change, accessing the key should raise a KeyError
        with pytest.raises(KeyError):
            plocal['test']

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProcessLocal___key_trans___0_test_edge_case.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal___key_trans___0_test_edge_case.py:3: in <module>
    from pytutils.mappings import ProcessLocal
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal___key_trans___0_test_edge_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""