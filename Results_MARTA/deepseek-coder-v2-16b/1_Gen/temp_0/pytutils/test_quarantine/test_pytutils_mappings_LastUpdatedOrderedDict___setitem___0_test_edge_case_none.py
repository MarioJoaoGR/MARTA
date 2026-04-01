
from pytutils.mappings import LastUpdatedOrderedDict
import pytest

def test_edge_case_none():
    ld = LastUpdatedOrderedDict()
    ld['a'] = 1
    ld['b'] = 2
    assert list(ld.keys()) == ['a', 'b']
    
    ld['a'] = 4  # Updating the value of key 'a'
    assert list(ld.keys()) == ['b', 'a']

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_LastUpdatedOrderedDict___setitem___0_test_edge_case_none.py _
pytutils/Test4DT_tests/test_pytutils_mappings_LastUpdatedOrderedDict___setitem___0_test_edge_case_none.py:2: in <module>
    from pytutils.mappings import LastUpdatedOrderedDict
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_LastUpdatedOrderedDict___setitem___0_test_edge_case_none.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""