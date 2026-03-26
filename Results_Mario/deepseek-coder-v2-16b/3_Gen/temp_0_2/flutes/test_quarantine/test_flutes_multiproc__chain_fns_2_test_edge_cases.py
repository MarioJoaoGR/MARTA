
from typing import List, Callable, Tuple, Any, Dict

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_2_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_2_test_edge_cases.py:4:39: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_2_test_edge_cases.py:4:113: E0602: Undefined variable 'R' (undefined-variable)


"""