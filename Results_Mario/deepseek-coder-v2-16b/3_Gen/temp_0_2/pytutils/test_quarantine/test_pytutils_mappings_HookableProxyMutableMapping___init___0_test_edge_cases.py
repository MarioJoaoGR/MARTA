
import pytest
from pytutils.mappings import HookableProxyMutableMapping

def test_hookable_proxy_mutable_mapping():
    my_dict = {'a': 1, 'b': 2}
    proxy_map = HookableProxyMutableMapping(my_dict)
    
    # Check the initial representation
    assert str(proxy_map) == repr(my_dict)
    
    # Add a new item
    proxy_map['c'] = 3
    assert 'c' in proxy_map and proxy_map['c'] == 3
    
    # Delete an item
    del proxy_map['a']
    assert 'a' not in proxy_map

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___init___0_test_edge_cases.py _
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___init___0_test_edge_cases.py:3: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___init___0_test_edge_cases.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""