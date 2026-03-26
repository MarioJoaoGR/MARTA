
from pytutils.mappings import HookableProxyMutableMapping

def test_edge_case_none():
    my_dict = {'a': 1, 'b': 2}
    proxy_map = HookableProxyMutableMapping(my_dict)
    
    # Test iteration with no keys allowed
    class NoKeyAllowed(HookableProxyMutableMapping):
        def __key_allowed__(self, key):
            return False
    
    no_keys_map = NoKeyAllowed(my_dict)
    assert list(no_keys_map.__iter__()) == []

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___iter___0_test_edge_case_none.py _
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___iter___0_test_edge_case_none.py:2: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___iter___0_test_edge_case_none.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""