
import pytest
from pymonet.utils import curry

def add(a, b):
    return a + b

@pytest.mark.parametrize("args_count", [1, 2, 3])
def test_invalid_inputs(args_count):
    curried_add = curry(add, args_count=args_count)
    
    if args_count == 1:
        with pytest.raises(TypeError):
            curried_add(1)
    elif args_count == 2:
        assert curried_add(1)(2) == 3
    else:
        assert curried_add(1)(2)(3) == 6

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pyMonet/Test4DT_tests/test_pymonet_utils_fn_0_test_invalid_inputs.py ..F [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_inputs[3] ____________________________

args_count = 3

    @pytest.mark.parametrize("args_count", [1, 2, 3])
    def test_invalid_inputs(args_count):
        curried_add = curry(add, args_count=args_count)
    
        if args_count == 1:
            with pytest.raises(TypeError):
                curried_add(1)
        elif args_count == 2:
            assert curried_add(1)(2) == 3
        else:
>           assert curried_add(1)(2)(3) == 6

pyMonet/Test4DT_tests/test_pymonet_utils_fn_0_test_invalid_inputs.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/utils.py:20: in fn
    return x(*args)
pyMonet/pymonet/utils.py:21: in <lambda>
    return curry(lambda *args1: x(*(args + args1)), args_count - len(args))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args1 = (2, 3)

>   return curry(lambda *args1: x(*(args + args1)), args_count - len(args))
E   TypeError: add() takes 2 positional arguments but 3 were given

pyMonet/pymonet/utils.py:21: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_fn_0_test_invalid_inputs.py::test_invalid_inputs[3]
========================= 1 failed, 2 passed in 0.07s ==========================
"""