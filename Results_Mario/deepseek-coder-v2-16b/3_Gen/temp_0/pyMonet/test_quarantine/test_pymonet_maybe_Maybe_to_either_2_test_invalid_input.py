
import pytest
from pymonet.maybe import Maybe, Left, Right

def test_invalid_input():
    with pytest.raises(TypeError):
        Maybe(value='Invalid', is_nothing=None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_maybe_Maybe_to_either_2_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_either_2_test_invalid_input.py:3:0: E0611: No name 'Left' in module 'pymonet.maybe' (no-name-in-module)
pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_either_2_test_invalid_input.py:3:0: E0611: No name 'Right' in module 'pymonet.maybe' (no-name-in-module)


"""