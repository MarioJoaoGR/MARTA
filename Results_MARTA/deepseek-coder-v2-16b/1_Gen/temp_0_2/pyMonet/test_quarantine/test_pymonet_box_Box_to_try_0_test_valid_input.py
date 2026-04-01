
import pytest
from pymonet.monad_try import Try

@pytest.fixture
def box():
    return Box(42)

def test_valid_input(box):
    try_monad = box.to_try()
    assert try_monad.value == 42
    assert try_monad.is_success is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_to_try_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_box_Box_to_try_0_test_valid_input.py:7:11: E0602: Undefined variable 'Box' (undefined-variable)


"""