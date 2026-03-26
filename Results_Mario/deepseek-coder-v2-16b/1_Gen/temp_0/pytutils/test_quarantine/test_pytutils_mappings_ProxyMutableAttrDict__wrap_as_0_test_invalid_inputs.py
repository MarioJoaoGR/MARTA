
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_invalid_inputs():
    # Test initializing with None should raise a TypeError
    with pytest.raises(TypeError):
        ProxyMutableAttrDict(None)
    
    # Test initializing with an integer should raise a TypeError
    with pytest.raises(TypeError):
        ProxyMutableAttrDict(123)
    
    # Test initializing with a string should raise a TypeError
    with pytest.raises(TypeError):
        ProxyMutableAttrDict("invalid")
    
    # Test initializing with a list should raise a TypeError
    with pytest.raises(TypeError):
        ProxyMutableAttrDict([1, 2, 3])

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_invalid_inputs.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_invalid_inputs.py:3: in <module>
    from pytutils.mappings import ProxyMutableAttrDict
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_invalid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""