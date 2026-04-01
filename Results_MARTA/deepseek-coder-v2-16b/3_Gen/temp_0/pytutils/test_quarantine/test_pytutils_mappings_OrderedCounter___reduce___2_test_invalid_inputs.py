
import pytest
from pytutils.mappings import OrderedCounter

def test_invalid_inputs():
    with pytest.raises(AttributeError):
        oc = OrderedCounter()
        assert oc.__reduce__() == (OrderedCounter, (collections.OrderedDict(oc),))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_OrderedCounter___reduce___2_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_mappings_OrderedCounter___reduce___2_test_invalid_inputs.py:8:52: E0602: Undefined variable 'collections' (undefined-variable)


"""