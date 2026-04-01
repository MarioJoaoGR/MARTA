
import pytest
from pytutils.mappings import PrefixedProxyMutableMapping
from collections import defaultdict, OrderedDict

def test_edge_cases():
    # Test with an empty mapping
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {})
    assert len(prefixed_mapping) == 0
    
    # Test adding a key to an empty mapping
    prefixed_mapping['new_key'] = 123
    assert prefixed_mapping['pre_new_key'] == 123
    
    # Test getting a key that doesn't exist with only_prefixed=True
    with pytest.raises(KeyError):
        prefixed_mapping['non_existent_key']
    
    # Test setting a key without prefix when only_prefixed=True should raise an error
    with pytest.raises(KeyError):
        prefixed_mapping.__setitem__('non_existent_key', 456)
    
    # Test setting a key with the correct prefix
    prefixed_mapping['pre_existing_key'] = 456
    assert prefixed_mapping['pre_existing_key'] == 456
    
    # Test removing a key that exists and has the prefix
    del prefixed_mapping['pre_existing_key']
    with pytest.raises(KeyError):
        prefixed_mapping['pre_existing_key']
    
    # Test adding multiple keys to an empty mapping
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', defaultdict(int))
    for i in range(5):
        prefixed_mapping[f'key{i}'] = i * 100
    assert len(prefixed_mapping) == 5
    
    # Test setting a key with only_prefixed=False
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', OrderedDict([('existing_key', 1)]), only_prefixed=False)
    prefixed_mapping['no_prefix'] = 2
    assert prefixed_mapping['no_prefix'] == 2
    assert prefixed_mapping['pre_existing_key'] == 1
    
    # Test repr output for different configurations
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {'key4': 400})
    assert str(prefixed_mapping) == "{'pre_key4': 400}"
    
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {'key5': 500}, fancy_repr=False)
    assert str(prefixed_mapping) == "{'pre_key5': 500}"
    
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {'key6': 600}, dictify_repr=True)
    assert str(prefixed_mapping) == "OrderedDict([('pre_key6', 600)])"

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_trans___0_test_edge_cases.py _
pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_trans___0_test_edge_cases.py:3: in <module>
    from pytutils.mappings import PrefixedProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_trans___0_test_edge_cases.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""