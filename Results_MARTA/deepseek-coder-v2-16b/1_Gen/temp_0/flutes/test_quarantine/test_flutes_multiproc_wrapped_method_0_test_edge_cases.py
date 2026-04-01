
import pytest
from flutes.multiproc import wrapped_method, pool_method

@pytest.mark.parametrize("func, args, kwds", [
    (lambda x: x, (), {}),
    (lambda x, y=0: x + y, (1,), {'y': 2}),
    (lambda *args, **kwargs: sum(kwargs.values()), (), {'a': 1, 'b': 2, 'c': 3})
])
def test_wrapped_method(func, args, kwds):
    wrapped = wrapped_method(func, *args, args=args, kwds=kwds)
    assert wrapped() == func(*args, **kwds)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_wrapped_method_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_wrapped_method_0_test_edge_cases.py:3:0: E0611: No name 'wrapped_method' in module 'flutes.multiproc' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_wrapped_method_0_test_edge_cases.py:3:0: E0611: No name 'pool_method' in module 'flutes.multiproc' (no-name-in-module)


"""