
import pytest
from pytutils.mappings import PrefixedProxyMutableMapping
from unittest.mock import Mock

def test_valid_input():
    # Create a mock dictionary-like object
    mock_mapping = Mock()
    mock_mapping.__contains__ = Mock(return_value=True)
    mock_mapping.__getitem__ = Mock(return_value='value')
    mock_mapping.__setitem__ = Mock()
    mock_mapping.keys = Mock(return_value=['key'])
    
    # Initialize the PrefixedProxyMutableMapping with a prefix and the mock mapping
    prefixed_proxy = PrefixedProxyMutableMapping('pre_', mock_mapping)
    
    # Assert that the __prefix is set correctly
    assert prefixed_proxy._PrefixedProxyMutableMapping__prefix == 'pre_'
    
    # Test adding a new key with the prefix
    prefixed_proxy['new_key'] = 'new_value'
    mock_mapping.__setitem__.assert_called_with('pre_new_key', 'new_value')
    
    # Test accessing an existing key with the prefix
    assert prefixed_proxy['pre_key'] == 'value'
    mock_mapping.__getitem__.assert_called_with('pre_key')
    
    # Test removing a key with the prefix
    del prefixed_proxy['pre_key']
    mock_mapping.pop.assert_called_with('pre_key')

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_add_prefix___0_test_valid_input.py _
pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_add_prefix___0_test_valid_input.py:3: in <module>
    from pytutils.mappings import PrefixedProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_add_prefix___0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""