
from pytutils.mappings import ProxyMutableMapping

def test_invalid_input():
    a = {}  # An empty dictionary to simulate the underlying mapping
    b = ProxyMutableMapping(a)
    
    try:
        item = b['non_existent_key']  # Attempting to get an invalid key
    except KeyError as e:
        assert str(e) == "'non_existent_key'", f"Expected 'KeyError' with message 'non_existent_key', but got {str(e)}"

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___getitem___0_test_invalid_input.py _
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___getitem___0_test_invalid_input.py:2: in <module>
    from pytutils.mappings import ProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___getitem___0_test_invalid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""