
import pytest
from flutes.multiproc import PoolType

def test_invalid_inputs():
    pool = PoolType()
    with pytest.raises(TypeError):
        # This should raise a TypeError because `fn` is not provided
        list(pool.imap_unordered())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_imap_unordered_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_invalid_inputs.py:9:13: E1120: No value for argument 'fn' in method call (no-value-for-parameter)
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_invalid_inputs.py:9:13: E1120: No value for argument 'iterable' in method call (no-value-for-parameter)


"""