
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPoolType, PoolState

class TestStatefulPoolType:
    def test_gather(self):
        class State(PoolState):
            def __init__(self):
                self.data = []
            
            def process_item(self, item):
                self.data.append(item)
                return item
        
        pool = StatefulPoolType(State)
        results = pool.gather(State().process_item, [1, 2, 3, 4], chunksize=2)
        assert list(results) == [1, 2, 3, 4]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPoolType_gather_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_gather_0_test_edge_cases.py:17:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""