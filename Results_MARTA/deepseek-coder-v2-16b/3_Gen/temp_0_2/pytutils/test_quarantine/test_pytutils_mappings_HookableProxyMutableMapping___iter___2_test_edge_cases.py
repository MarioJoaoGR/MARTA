
from pytutils.mappings import HookableProxyMutableMapping

class MyHookableMapping(HookableProxyMutableMapping):
    def __key_allowed__(self, key):
        # Allow only integer keys and 'foo' specifically
        return isinstance(key, int) or key == 'foo'

    def __key_remove_prefix__(self, key):
        # Implement prefix removal logic if needed
        return key  # Default implementation does nothing

my_mapping = {'foo': 42}
hookable_map = MyHookableMapping(my_mapping)

# Test the iteration functionality
def test_iteration():
    assert list(hookable_map.__iter__()) == ['foo']

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___iter___2_test_edge_cases.py _
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___iter___2_test_edge_cases.py:2: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___iter___2_test_edge_cases.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""