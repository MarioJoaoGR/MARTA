
import pytest
from multiprocessing import Pool, PoolState
from flutes.multiproc import StatefulPoolType

@pytest.fixture(scope="module")
def pool():
    class MyState(PoolState):
        def __init__(self):
            self.data = []
        
        def process_item(self, item):
            self.data.append(item * 2)
    
    return StatefulPoolType(MyState)

def test_map_async(pool):
    results = pool.map_async(lambda s, x: s.process_item(x), range(10), chunksize=2).get()
    assert results == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPoolType_map_async_0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_map_async_0_test_edge_case.py:3:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)


"""