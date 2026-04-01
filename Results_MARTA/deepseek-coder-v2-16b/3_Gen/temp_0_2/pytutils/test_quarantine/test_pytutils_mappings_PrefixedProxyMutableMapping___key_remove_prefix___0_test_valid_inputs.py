
import pytest
from pytutils.mappings import PrefixedProxyMutableMapping
from collections import defaultdict, OrderedDict

def test_valid_inputs():
    # Test with an OrderedDict
    my_dict = OrderedDict([('foo', 1), ('bar', 2)])
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', my_dict)
    assert str(prefixed_mapping) == "{'_foo': 1, '_bar': 2}"
    
    # Test with a defaultdict
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', defaultdict(int))
    prefixed_mapping['key1'] = 10
    assert str(prefixed_mapping) == "{'pre_key1': 10}"
    
    # Test with a regular dict
    my_dict = {'foo': 1, 'bar': 2}
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', my_dict)
    assert str(prefixed_mapping) == "{'_foo': 1, '_bar': 2}"
    
    # Test with only_prefixed=False
    my_dict = {'key4': 40, 'pre_key5': 50}
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', my_dict, only_prefixed=False)
    assert str(prefixed_mapping) == "{'key4': 40, 'pre_key5': 50}"
    
    # Test with dictify_repr=True
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', {'foo': 1, 'bar': 2}, dictify_repr=True)
    assert isinstance(eval(str(prefixed_mapping)), dict)

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_valid_inputs.py _
pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_valid_inputs.py:3: in <module>
    from pytutils.mappings import PrefixedProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_valid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""