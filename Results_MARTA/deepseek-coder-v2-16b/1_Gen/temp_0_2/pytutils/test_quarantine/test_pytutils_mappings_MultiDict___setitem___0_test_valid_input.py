
import pytest
from pytutils.mappings import MultiDict

def test_valid_input():
    md = MultiDict()
    md['key1'] = 'value1'
    md['key2'] = {'nested_key': 'nested_value'}
    
    assert len(md) == 3, "Expected the dictionary to have 3 keys after adding two unique keys and one nested key."
    assert isinstance(md['key1'], str), "Expected 'key1' to be a string."
    assert isinstance(md['key2'], dict), "Expected 'key2' to be a dictionary."
    assert len(md) == 3, "After adding another unique key, the count should still be 3."
    
    md['key2'] = 'new_value'
    assert len(md) == 4, "Expected the dictionary to have 4 keys after updating 'key2'."
    assert isinstance(md['key2'], str), "After updating, 'key2' should be a string."
    
    print(md)  # For debugging purposes if needed.

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_MultiDict___setitem___0_test_valid_input.py _
pytutils/Test4DT_tests/test_pytutils_mappings_MultiDict___setitem___0_test_valid_input.py:3: in <module>
    from pytutils.mappings import MultiDict
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_MultiDict___setitem___0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""