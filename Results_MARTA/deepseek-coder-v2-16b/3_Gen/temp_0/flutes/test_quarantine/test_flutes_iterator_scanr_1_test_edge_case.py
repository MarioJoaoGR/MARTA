
import pytest
from flutes.iterator import scanl

def test_edge_case():
    with pytest.raises(NotImplementedError):
        # Since the function is not implemented, we expect a NotImplementedError to be raised
        scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd'])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_scanr_1_test_edge_case
flutes/Test4DT_tests/test_flutes_iterator_scanr_1_test_edge_case.py:8:8: E0602: Undefined variable 'scanr' (undefined-variable)


"""