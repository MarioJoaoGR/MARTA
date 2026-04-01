
from pytutils.mappings import HookableProxyMutableMapping
import pytest

def test_edge_case():
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    proxy_map = HookableProxyMutableMapping(my_dict)
    
    # Test the edge case where all keys are allowed and no prefix is removed
    assert list(proxy_map.__iter__()) == ['key1', 'key2']

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___iter___0_test_edge_case.py _
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___iter___0_test_edge_case.py:2: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___iter___0_test_edge_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""