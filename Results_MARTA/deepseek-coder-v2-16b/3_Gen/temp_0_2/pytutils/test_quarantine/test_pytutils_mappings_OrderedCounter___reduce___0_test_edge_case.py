
import pytest
from pytutils.mappings import OrderedCounter
import collections

def test_OrderedCounter_reduce():
    # Create an instance of OrderedCounter with some data
    counter = OrderedCounter({'a': 1, 'b': 2})
    
    # Call the __reduce__ method and check its output
    result = counter.__reduce__()
    
    # Check that the result is a tuple containing (OrderedCounter, (OrderedDict(self),))
    assert isinstance(result[0], type)
    assert result[0] == OrderedCounter
    assert isinstance(result[1][0], collections.OrderedDict)
    assert list(result[1][0].items()) == [('a', 1), ('b', 2)]

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
=============================== 1 error in 0.14s ===============================
"""