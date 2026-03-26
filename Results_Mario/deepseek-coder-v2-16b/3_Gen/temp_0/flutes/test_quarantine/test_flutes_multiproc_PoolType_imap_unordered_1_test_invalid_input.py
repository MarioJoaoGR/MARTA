
import pytest
from flutes.multiproc import PoolType

def square(x):
    return x ** 2

@pytest.mark.parametrize("invalid_input", [None, "string", {"dict": True}])
def test_invalid_input(invalid_input):
    pool = PoolType()
    with pytest.raises(TypeError):
        result_iterator = pool.imap_unordered(square, invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_imap_unordered_1_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_1_test_invalid_input.py:12:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)

"""