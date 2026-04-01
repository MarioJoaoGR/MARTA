
import pytest
from pytutils.mappings import OrderedCounter
import collections

def test_OrderedCounter_reduce():
    oc = OrderedCounter()
    oc['a'] = 1
    oc['b'] = 2
    
    reduced_data = pickle.dumps(oc)
    restored_oc = pickle.loads(reduced_data)
    
    assert isinstance(restored_oc, OrderedCounter)
    assert dict(restored_oc) == {'a': 1, 'b': 2}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_OrderedCounter___reduce___0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_mappings_OrderedCounter___reduce___0_test_edge_case.py:11:19: E0602: Undefined variable 'pickle' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_mappings_OrderedCounter___reduce___0_test_edge_case.py:12:18: E0602: Undefined variable 'pickle' (undefined-variable)


"""