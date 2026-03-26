
import pytest
from pytutils.mappings import HookableProxyMutableMapping
from collections import UserDict

class MyMapping(UserDict):
    def __getitem__(self, key):
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __contains__(self, key):
        return super().__contains__(key)

    def __delitem__(self, key):
        super().__delitem__(key)

@pytest.fixture
def my_mapping():
    return MyMapping()

@pytest.fixture
def hookable_proxy(my_mapping):
    return HookableProxyMutableMapping(my_mapping)

def test_getitem(hookable_proxy, my_mapping):
    # Add a key to the mapping
    my_mapping['key'] = 'value'
    
    # Test getting the value using hookable proxy
    assert hookable_proxy['key'] == 'value'

def test_setitem(hookable_proxy, my_mapping):
    # Set a key in the hookable proxy
    hookable_proxy['new_key'] = 'new_value'
    
    # Check if the key is present in the mapping
    assert 'new_key' in hookable_proxy
    
    # Get the value to ensure it was set correctly
    assert hookable_proxy['new_key'] == 'new_value'

def test_delitem(hookable_proxy, my_mapping):
    # Add a key to the mapping
    my_mapping['delete_key'] = 'delete_value'
    
    # Delete the key using hookable proxy
    del hookable_proxy['delete_key']
    
    # Check if the key is not present in the mapping
    assert 'delete_key' not in hookable_proxy

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___getitem___0_test_edge_cases.py _
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___getitem___0_test_edge_cases.py:3: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___getitem___0_test_edge_cases.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""