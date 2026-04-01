
import pytest
from pytutils.mappings import PrefixedProxyMutableMapping

def test_edge_case():
    # Create a dictionary to wrap
    my_dict = {'foo': 1, 'bar': 2}
    
    # Test with only prefixed keys
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', my_dict)
    assert len(prefixed_mapping) == 2
    assert prefixed_mapping['pre_foo'] == 1
    assert 'foo' not in prefixed_mapping
    
    # Test with all keys allowed
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', my_dict, only_prefixed=False)
    assert len(prefixed_mapping) == 2
    assert prefixed_mapping['pre_foo'] == 1
    assert prefixed_mapping['foo'] == 1
    
    # Test with a key that doesn't have the prefix
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {'key': 'value'})
    with pytest.raises(KeyError):
        prefixed_mapping['key']

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_edge_case.py _
pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_edge_case.py:3: in <module>
    from pytutils.mappings import PrefixedProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_edge_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""