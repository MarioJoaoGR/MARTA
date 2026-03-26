
import pytest
from pytutils.mappings import ProxyMutableMapping

def test_init():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableMapping(a)
    
    assert isinstance(b, ProxyMutableMapping), "Instance should be of type ProxyMutableMapping"
    assert b._mapping == a, "The proxied dictionary should match the input dictionary"

def test_fancy_repr():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableMapping(a)
    
    expected_repr = "<ProxyMutableMapping {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}>"
    assert repr(b) == expected_repr, "Fancy repr should be as expected"

def test_dictify_repr():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableMapping(a, dictify_repr=True)
    
    expected_repr = "{'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}"
    assert repr(b) == expected_repr, "Dictified repr should be as expected"

def test_set_item():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableMapping(a)
    
    b['nice'] = False
    assert 'nice' in b._mapping, "The key 'nice' should be in the proxied dictionary"
    assert b._mapping['nice'] == False, "The value for key 'nice' should be False"

def test_get_item():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableMapping(a)
    
    assert b['whoa'] == True, "The value for key 'whoa' should be True"

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___init___0_test_edge_cases.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___init___0_test_edge_cases.py:3: in <module>
    from pytutils.mappings import ProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___init___0_test_edge_cases.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""