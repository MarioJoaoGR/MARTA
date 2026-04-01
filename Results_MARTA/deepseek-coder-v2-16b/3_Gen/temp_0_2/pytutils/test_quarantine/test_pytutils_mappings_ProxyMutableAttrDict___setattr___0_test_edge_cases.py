
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_setattr():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test setting a new attribute
    b.new_attr = "test"
    assert hasattr(b, 'new_attr')
    assert b.new_attr == "test"
    
    # Test setting an existing key with different value
    b.whoa = "yeee"
    assert b.whoa == "yeee"
    
    # Test setting a nested attribute
    b.subdict = dict(test=True)
    assert hasattr(b, 'subdict')
    assert b.subdict['test'] is True
    
    # Test setting an existing key with the same value (should not change)
    b.whoa = "yeee"
    assert b.whoa == "yeee"
    
    # Test setting a non-existent key without recursion enabled
    with pytest.raises(AttributeError):
        b.__recursion = False
        b.non_existent_key = "value"

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
=============================== 1 error in 0.15s ===============================
"""