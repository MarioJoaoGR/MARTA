
import pytest
from pytutils.mappings import OrderedCounter

def test_invalid_input():
    with pytest.raises(AttributeError):
        oc = OrderedCounter()
        oc['a'] = 1
        oc['b'] = 2
        reduced_data = pickle.dumps(oc)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_OrderedCounter___reduce___2_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_mappings_OrderedCounter___reduce___2_test_invalid_input.py:10:23: E0602: Undefined variable 'pickle' (undefined-variable)


"""