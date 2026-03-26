
import pytest
from pytutils.mappings import ProxyMutableMapping

def test_valid_case():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableMapping(a)
    
    # Check the initial representation
    assert str(b) == "<ProxyMutableAttrDict {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}>"
    
    # Modify the proxy and check if changes are reflected in the underlying dictionary
    b['nice'] = False
    b['whoa'] = 'yeee'
    
    assert str(b) == "<ProxyMutableAttrDict {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False}>"
    assert a == {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False}

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping__set_mapping_0_test_valid_case.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping__set_mapping_0_test_valid_case.py:3: in <module>
    from pytutils.mappings import ProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping__set_mapping_0_test_valid_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""