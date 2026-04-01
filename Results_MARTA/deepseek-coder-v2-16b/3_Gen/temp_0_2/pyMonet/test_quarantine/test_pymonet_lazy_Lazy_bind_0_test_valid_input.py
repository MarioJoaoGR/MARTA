
import pytest
from pymonet.lazy import Lazy

def test_valid_input():
    lazy_value = Lazy(lambda x: x * x)  # Example function to be called lazily
    result = lazy_value.bind(lambda x: Lazy(lambda y: x * y))(10)
    assert not result.is_evaluated

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_bind_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_valid_input.py:7:13: E1102: lazy_value.bind(lambda x: Lazy(lambda y: x * y)) is not callable (not-callable)


"""