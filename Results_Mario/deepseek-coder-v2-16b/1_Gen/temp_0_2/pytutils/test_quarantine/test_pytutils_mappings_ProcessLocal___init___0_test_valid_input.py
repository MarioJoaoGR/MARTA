
# Import ProcessLocal from pytutils.mappings
from pytutils.mappings import ProcessLocal
import os
import pytest

def test_valid_input():
    # Create an instance of ProcessLocal with a mock factory function
    plocal = ProcessLocal(mapping_factory=lambda: {})
    
    # Set a value in the process local storage
    plocal['test'] = True
    
    # Check if the value is correctly set
    assert plocal['test'] == True
    
    # Emulate a PID change by forcing it to be something invalid
    plocal._handle_pid(new_pid=-1)
    
    # Check if the mapping wipes itself since PID is different than what's stored
    with pytest.raises(KeyError):
        print(plocal['test'])

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProcessLocal___init___0_test_valid_input.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal___init___0_test_valid_input.py:3: in <module>
    from pytutils.mappings import ProcessLocal
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal___init___0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""