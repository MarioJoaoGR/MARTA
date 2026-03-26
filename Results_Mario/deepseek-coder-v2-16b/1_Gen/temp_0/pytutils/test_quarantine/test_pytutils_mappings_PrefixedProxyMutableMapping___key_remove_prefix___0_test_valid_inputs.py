
from pytutils.mappings import PrefixedProxyMutableMapping
import pytest

def test_valid_inputs():
    # Create a mock dictionary-like object for testing
    data = {'foo': 1, 'bar': 2}
    prefixed_dict = PrefixedProxyMutableMapping('pre_', data)
    
    # Test adding a new key with the prefix
    prefixed_dict['new_key'] = 3
    assert prefixed_dict['pre_new_key'] == 3
    
    # Test accessing an existing key with the prefix
    assert prefixed_dict['pre_foo'] == 1
    
    # Test removing a key with the prefix
    del prefixed_dict['pre_foo']
    with pytest.raises(KeyError):
        prefixed_dict['pre_foo']

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
pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_valid_inputs.py:2: in <module>
    from pytutils.mappings import PrefixedProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_remove_prefix___0_test_valid_inputs.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""