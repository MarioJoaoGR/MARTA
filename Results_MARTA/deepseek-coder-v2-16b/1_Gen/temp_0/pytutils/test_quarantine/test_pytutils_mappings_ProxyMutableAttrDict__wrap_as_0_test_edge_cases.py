
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_edge_cases():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test setting and getting values through key-based access
    assert 'whoa' in b  # Check if the attribute is present
    assert b['whoa'] == True  # Check the value of the attribute
    
    b['nice'] = False
    assert b['nice'] == False  # Verify that the change is reflected
    
    # Test setting and getting values through attribute-style access
    assert hasattr(b, 'whoa')  # Check if the attribute is present
    assert getattr(b, 'whoa') == True  # Check the value of the attribute
    
    setattr(b, 'state', 'new')
    assert b.state == 'new'  # Verify that the change is reflected
    
    # Test recursion
    b.subdict = dict(test=True)
    assert hasattr(b, 'subdict')  # Check if the attribute is present
    assert getattr(b.subdict, 'test') == True  # Check the value of the nested attribute

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_edge_cases.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_edge_cases.py:3: in <module>
    from pytutils.mappings import ProxyMutableAttrDict
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_edge_cases.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""