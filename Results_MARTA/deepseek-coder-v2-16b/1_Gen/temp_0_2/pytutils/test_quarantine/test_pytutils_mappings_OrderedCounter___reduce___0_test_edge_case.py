
import pytest
from pytutils.mappings import OrderedCounter
import collections

def test_reduce():
    # Create an instance of OrderedCounter
    oc = OrderedCounter([1, 2, 3, 4])
    
    # Call the __reduce__ method and check the result
    reduce_result = oc.__reduce__()
    
    # Assert that the result is a tuple with the correct class and an OrderedDict initialized with the current state of the OrderedCounter instance
    assert isinstance(reduce_result, tuple)
    assert reduce_result[0] == OrderedCounter
    assert isinstance(reduce_result[1][0], collections.OrderedDict)
    
    # Check if the OrderedDict contains the same elements as the OrderedCounter
    assert list(reduce_result[1][0].items()) == [(1, 1), (2, 1), (3, 1), (4, 1)]

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
_ ERROR collecting Test4DT_tests/test_pytutils_mappings_OrderedCounter___reduce___0_test_edge_case.py _
pytutils/Test4DT_tests/test_pytutils_mappings_OrderedCounter___reduce___0_test_edge_case.py:3: in <module>
    from pytutils.mappings import OrderedCounter
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_mappings_OrderedCounter___reduce___0_test_edge_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""