
# Importing the necessary module from pytutils
from pytutils.mappings import HookableProxyMutableMapping

def test_key_allowed():
    # Create an instance of HookableProxyMutableMapping with a sample dictionary
    mapping = {'key1': 'value1', 'key2': 'value2'}
    proxy_map = HookableProxyMutableMapping(mapping)
    
    # Test the default behavior where all keys are allowed
    assert proxy_map.__key_allowed__('any_key') is True

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_allowed___0_test_edge_case.py _
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_allowed___0_test_edge_case.py:3: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_allowed___0_test_edge_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""