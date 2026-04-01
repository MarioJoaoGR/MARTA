
import pytest
from pytutils.mappings import MultiDict

def test_setitem_edge_case():
    md = MultiDict()
    # First assignment should not change the key
    md['key1'] = 'value1'
    assert str(md) == "{'key1': 'value1'}"
    
    # Second assignment with a nested dictionary should add a unique suffix to the key
    md['key2'] = {'nested_key': 'nested_value'}
    expected_str = "{'key1': 'value1', 'key2': {'nested_key': 'nested_value'}}"
    assert str(md) == expected_str, f"Expected {expected_str}, but got {str(md)}"
    
    # Third assignment with another nested dictionary should add a new unique suffix to the key
    md['key2'] = {'another_nested_key': 'another_nested_value'}
    expected_str = "{'key1': 'value1', 'key2': {'nested_key': 'nested_value', 'key3': {'another_nested_key': 'another_nested_value'}}}"
    assert str(md) == expected_str, f"Expected {expected_str}, but got {str(md)}"

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_MultiDict___setitem___0_test_edge_case.py _
pytutils/Test4DT_tests/test_pytutils_mappings_MultiDict___setitem___0_test_edge_case.py:3: in <module>
    from pytutils.mappings import MultiDict
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_MultiDict___setitem___0_test_edge_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""