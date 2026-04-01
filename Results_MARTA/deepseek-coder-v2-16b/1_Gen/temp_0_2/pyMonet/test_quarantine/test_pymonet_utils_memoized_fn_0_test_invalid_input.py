
import pytest
from pymonet.utils import memoized_fn, cache, fn, key, find

@pytest.mark.parametrize("argument", [None, 1, "string", {"key": "value"}, [1, 2, 3], (1, 2, 3)])
def test_invalid_input(argument):
    with pytest.raises(TypeError):
        memoized_fn(argument)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_utils_memoized_fn_0_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_utils_memoized_fn_0_test_invalid_input.py:3:0: E0611: No name 'memoized_fn' in module 'pymonet.utils' (no-name-in-module)
pyMonet/Test4DT_tests/test_pymonet_utils_memoized_fn_0_test_invalid_input.py:3:0: E0611: No name 'cache' in module 'pymonet.utils' (no-name-in-module)
pyMonet/Test4DT_tests/test_pymonet_utils_memoized_fn_0_test_invalid_input.py:3:0: E0611: No name 'fn' in module 'pymonet.utils' (no-name-in-module)
pyMonet/Test4DT_tests/test_pymonet_utils_memoized_fn_0_test_invalid_input.py:3:0: E0611: No name 'key' in module 'pymonet.utils' (no-name-in-module)


"""