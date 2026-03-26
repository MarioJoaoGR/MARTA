
import pytest
from pytutils.iters import dedupe_iter

def test_dedupe():
    def my_func():
        return [1, 2, 3, 2, 1]
    
    @pytest.mark.parametrize("instance", [None])
    @pytest.mark.parametrize("args", [((),)])
    @pytest.mark.parametrize("kwargs", [{}, {'instance': None}])
    def test_dedupe_with_params(instance, args, kwargs):
        decorated = dedupe(my_func, instance, *args, **kwargs)
        assert list(decorated()) == [1, 2, 3]
    
    test_dedupe_with_params()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_iters_dedupe_2_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_iters_dedupe_2_test_edge_cases.py:13:20: E0602: Undefined variable 'dedupe' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_iters_dedupe_2_test_edge_cases.py:16:4: E1120: No value for argument 'instance' in function call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_iters_dedupe_2_test_edge_cases.py:16:4: E1120: No value for argument 'args' in function call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_iters_dedupe_2_test_edge_cases.py:16:4: E1120: No value for argument 'kwargs' in function call (no-value-for-parameter)


"""