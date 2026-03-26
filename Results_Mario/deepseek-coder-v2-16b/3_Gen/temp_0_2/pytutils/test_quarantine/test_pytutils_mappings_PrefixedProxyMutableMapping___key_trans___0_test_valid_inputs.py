
import pytest
from pytutils.mappings import PrefixedProxyMutableMapping
from collections import defaultdict, OrderedDict

def test_valid_inputs():
    # Test with an OrderedDict
    my_dict = OrderedDict([('foo', 1), ('bar', 2)])
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', my_dict)
    assert len(prefixed_mapping) == 2
    assert list(prefixed_mapping.keys()) == ['pre_foo', 'pre_bar']
    
    # Test with a defaultdict
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', defaultdict(int))
    prefixed_mapping['key1'] = 10
    assert prefixed_mapping['pre_key1'] == 10
    
    # Test with an existing mapping
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {'key2': 20})
    assert prefixed_mapping['pre_key2'] == 20
    
    # Test with only_prefixed=False
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {'key3': 30}, only_prefixed=False)
    prefixed_mapping['no_prefix'] = 40
    assert list(prefixed_mapping.keys()) == ['pre_key3', 'no_prefix']
    
    # Test with dictify_repr=True
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {'key4': 40}, dictify_repr=True)
    assert isinstance(prefixed_mapping, dict)
    assert list(prefixed_mapping.keys()) == ['pre_key4']
    
    # Test with fancy_repr=False and dictify_repr=False
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {'key5': 50}, fancy_repr=False, dictify_repr=False)
    assert repr(prefixed_mapping) == "{'pre_key5': 50}"

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_trans___0_test_valid_inputs.py _
pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_trans___0_test_valid_inputs.py:3: in <module>
    from pytutils.mappings import PrefixedProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_trans___0_test_valid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""