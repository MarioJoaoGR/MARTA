
from flutes.multiproc import PoolType
import pytest
from typing import Callable, Iterable, List, Optional, Any, Mapping

class TestPoolTypeMap:
    def test_valid_inputs(self):
        pool = PoolType()
        
        def square(x):
            return x ** 2
        
        result = pool.map(square, [1, 2, 3, 4])
        assert result == [1, 4, 9, 16]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_map_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_0_test_valid_inputs.py:13:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""