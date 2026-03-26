
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_valid_inputs():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Check if the initialization works correctly
    assert isinstance(b, ProxyMutableAttrDict), "Instance should be of type ProxyMutableAttrDict"
    assert b.__mapping == a, "The mapping should be equal to the input dictionary"
    assert b.__recursion is True, "Recursion should be enabled by default"
    
    # Check attribute-style access and modification
    b.state = 'new'
    assert hasattr(b, 'state'), "Attribute 'state' should exist on the instance"
    assert getattr(b, 'state') == 'new', "The value of 'state' should be 'new'"
    
    # Check nested attribute access and modification
    b.subdict = dict(test=True)
    assert hasattr(b, 'subdict'), "Attribute 'subdict' should exist on the instance"
    assert isinstance(getattr(b, 'subdict'), ProxyMutableAttrDict), "Subdict should be a ProxyMutableAttrDict instance"
    assert getattr(b.subdict, 'test') is True, "The value of 'subdict.test' should be True"
    
    # Check if changes are reflected in the underlying mapping
    b['nice'] = False
    assert 'nice' in b.__mapping, "Key 'nice' should exist in the underlying mapping"
    assert b.__mapping['nice'] is False, "The value of 'nice' should be False"
    
    # Check if changes are reflected through attribute-style access
    b.whoa = 'yeee'
    assert getattr(b, 'whoa') == 'yeee', "The value of 'whoa' should be 'yeee'"

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_valid_inputs.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_valid_inputs.py:3: in <module>
    from pytutils.mappings import ProxyMutableAttrDict
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_valid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""