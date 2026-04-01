
import pytest
from pytutils.mappings import PrefixedProxyMutableMapping
from collections import defaultdict, OrderedDict

def test_valid_input():
    # Test with a regular dictionary
    my_dict = {'foo': 1, 'bar': 2}
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', my_dict)
    assert dict(prefixed_mapping) == {'_foo': 1, '_bar': 2}
    
    # Test with only_prefixed=False
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', my_dict, only_prefixed=False)
    assert dict(prefixed_mapping) == {'foo': 1, 'bar': 2, '_foo': 1, '_bar': 2}
    
    # Test with a defaultdict
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', defaultdict(int))
    prefixed_mapping['key1'] = 10
    assert dict(prefixed_mapping) == {'pre_key1': 10}
    
    # Test with an existing mapping
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {'key2': 20})
    assert prefixed_mapping['pre_key2'] == 20
    
    # Test with only_prefixed=False and adding a non-prefixed key
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {'key3': 30}, only_prefixed=False)
    prefixed_mapping['no_prefix'] = 40
    assert dict(prefixed_mapping) == {'pre_key3': 30, 'no_prefix': 40}

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_valid_input.py _
pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_valid_input.py:3: in <module>
    from pytutils.mappings import PrefixedProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""