
import pytest
from pytutils.mappings import HookableProxyMutableMapping

def test_valid_input():
    # Create a sample dictionary to wrap with our HookableProxyMutableMapping
    sample_dict = {'key1': 'value1', 'key2': 'value2'}
    
    # Instantiate the HookableProxyMutableMapping with the sample dictionary
    proxy_map = HookableProxyMutableMapping(sample_dict)
    
    # Ensure that the initial length of the dictionary is 2
    assert len(proxy_map) == 2, "Initial length of the dictionary should be 2"
    
    # Delete an item from the mapping and check if it's removed correctly
    del proxy_map['key1']
    assert 'key1' not in proxy_map, "'key1' should have been deleted from the mapping"
    
    # Ensure that the length of the dictionary is now 1 after deletion
    assert len(proxy_map) == 1, "Length of the dictionary should be 1 after deleting one item"

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___delitem___0_test_valid_input.py _
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___delitem___0_test_valid_input.py:3: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___delitem___0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""