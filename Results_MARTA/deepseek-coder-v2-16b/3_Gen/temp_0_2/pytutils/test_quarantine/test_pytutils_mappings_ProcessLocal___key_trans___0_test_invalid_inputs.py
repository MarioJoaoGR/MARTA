
import pytest
from pytutils.mappings import ProcessLocal

def test_invalid_inputs():
    plocal = ProcessLocal()
    
    with pytest.raises(KeyError):
        # Simulate a PID change by forcing it to be something invalid
        plocal._handle_pid(new_pid=-1)
        plocal['test']  # This should raise KeyError since the mapping has been wiped

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProcessLocal___key_trans___0_test_invalid_inputs.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal___key_trans___0_test_invalid_inputs.py:3: in <module>
    from pytutils.mappings import ProcessLocal
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal___key_trans___0_test_invalid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""