
from pytutils.mappings import HookableProxyMutableMapping
import pytest

def test_valid_input():
    # Create a valid dictionary for testing
    mapping = {'key1': 'value1', 'key2': 'value2'}
    
    # Instantiate the HookableProxyMutableMapping with the valid dictionary
    proxy_map = HookableProxyMutableMapping(mapping)
    
    # Check if the instance is correctly initialized
    assert isinstance(proxy_map, HookableProxyMutableMapping), "Instance should be a HookableProxyMutableMapping"
    
    # Test getting an item from the mapping
    assert proxy_map['key1'] == 'value1', "Getting key1 should return value1"
    
    # Test setting a new item in the mapping
    proxy_map['key3'] = 'value3'
    assert 'key3' in proxy_map, "After setting key3, it should be in the mapping"
    assert proxy_map['key3'] == 'value3', "Getting key3 should return value3"
    
    # Test deleting an item from the mapping
    del proxy_map['key2']
    with pytest.raises(KeyError):
        print(proxy_map['key2'])  # This should raise a KeyError since 'key2' has been deleted

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_allowed___0_test_valid_input.py _
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_allowed___0_test_valid_input.py:2: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_allowed___0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""