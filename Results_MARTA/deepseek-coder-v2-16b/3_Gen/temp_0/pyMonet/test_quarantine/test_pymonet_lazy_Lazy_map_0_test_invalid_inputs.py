
import pytest
from pymonet.lazy import Lazy

@pytest.mark.parametrize("invalid_input", [123, "string", None])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        lazy = Lazy(lambda x: x)  # Any function will do here since we expect a TypeError regardless of the function
        if invalid_input is not None:
            lazy.map(lambda x: x)(invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_map_0_test_invalid_inputs
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_map_0_test_invalid_inputs.py:10:12: E1102: lazy.map(lambda x: x) is not callable (not-callable)


"""