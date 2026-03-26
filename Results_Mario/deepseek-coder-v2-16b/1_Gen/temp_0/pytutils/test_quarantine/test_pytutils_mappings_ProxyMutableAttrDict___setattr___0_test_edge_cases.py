
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_setattr():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Setting an attribute directly should work and reflect in the dictionary
    b.state = 'new'
    assert b['state'] == 'new', "Setting attribute did not update the underlying dictionary."
    
    # Setting a nested attribute should create a new ProxyMutableAttrDict instance
    b.subdict = dict(test=True)
    assert isinstance(b.subdict, ProxyMutableAttrDict), "Nested attributes are not being handled correctly."
    assert b.subdict['test'] == True, "Setting nested attributes did not update the underlying dictionary correctly."
    
    # Attempting to set an attribute that does not exist should raise AttributeError
    with pytest.raises(AttributeError):
        b.non_existent_attribute = 'value'

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___setattr___0_test_edge_cases.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___setattr___0_test_edge_cases.py:3: in <module>
    from pytutils.mappings import ProxyMutableAttrDict
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___setattr___0_test_edge_cases.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""