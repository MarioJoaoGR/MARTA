
import pytest
from typing import Callable, Iterable

def scanl(func: Callable[[B, A], B], iterable: Iterable[A], initial: B) -> Iterator[B]:
    result = []
    acc = initial
    for item in iterable:
        acc = func(acc, item)
        result.append(acc)
    return iter(result)

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test when func is not a callable
        list(scanl('not_a_function', [1, 2, 3, 4], 0))
    
    with pytest.raises(TypeError):
        # Test when iterable is not an iterable
        list(scanl(lambda x, y: x + y, 123, 0))
    
    with pytest.raises(TypeError):
        # Test when initial value is of incorrect type
        list(scanl(lambda x, y: x + y, [1, 2, 3, 4], "initial"))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_scanl_2_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_invalid_inputs.py:5:26: E0602: Undefined variable 'B' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_invalid_inputs.py:5:29: E0602: Undefined variable 'A' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_invalid_inputs.py:5:33: E0602: Undefined variable 'B' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_invalid_inputs.py:5:56: E0602: Undefined variable 'A' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_invalid_inputs.py:5:69: E0602: Undefined variable 'B' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_invalid_inputs.py:5:75: E0602: Undefined variable 'Iterator' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_invalid_inputs.py:5:84: E0602: Undefined variable 'B' (undefined-variable)


"""