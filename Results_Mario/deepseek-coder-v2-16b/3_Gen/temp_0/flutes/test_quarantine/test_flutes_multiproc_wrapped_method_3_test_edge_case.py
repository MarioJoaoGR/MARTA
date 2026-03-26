
import pytest
from flutes.multiproc import wrapped_method  # Importing the wrapped_method function

def test_edge_case():
    def multiply(a, b):
        return a * b
    
    result = wrapped_method(multiply, 5, b=10)
    assert result == 50

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_wrapped_method_3_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_wrapped_method_3_test_edge_case.py:3:0: E0611: No name 'wrapped_method' in module 'flutes.multiproc' (no-name-in-module)


"""