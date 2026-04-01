
import pytest
from unittest.mock import patch
from pytutils.mappings import OrderedCounter

@patch('pytutils.mappings.collections')
def test_OrderedCounter_repr(mock_collections):
    # Mocking the OrderedDict from collections to avoid actual module dependency issues during testing
    mock_collections.OrderedDict = type('OrderedDict', (), {})
    
    oc = OrderedCounter()
    oc['apple'] += 1
    oc['banana'] += 1
    
    expected_repr = "OrderedCounter({'apple': 1, 'banana': 1})"
    assert repr(oc) == expected_repr

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_OrderedCounter___repr___0_test_valid_input.py _
pytutils/Test4DT_tests/test_pytutils_mappings_OrderedCounter___repr___0_test_valid_input.py:4: in <module>
    from pytutils.mappings import OrderedCounter
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_OrderedCounter___repr___0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""