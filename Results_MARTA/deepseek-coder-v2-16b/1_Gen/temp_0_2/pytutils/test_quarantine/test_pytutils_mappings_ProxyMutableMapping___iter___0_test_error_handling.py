
import pytest
from pytutils.mappings import ProxyMutableMapping

def test_error_handling():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableMapping(a)
    
    # Test the __iter__ method to ensure it correctly iterates over the keys of the mapping
    expected_keys = set(a.keys())
    actual_keys = {key for key in b}
    
    assert expected_keys == actual_keys, "The iterator does not return the correct keys."

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___iter___0_test_error_handling.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___iter___0_test_error_handling.py:3: in <module>
    from pytutils.mappings import ProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___iter___0_test_error_handling.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""