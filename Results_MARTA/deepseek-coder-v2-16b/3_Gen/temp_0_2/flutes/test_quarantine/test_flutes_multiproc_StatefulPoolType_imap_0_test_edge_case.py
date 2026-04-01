
import pytest
from multiprocessing import PoolState
from flutes.multiproc import StatefulPoolType

@pytest.fixture
def pool():
    class MyState(PoolState):
        def process_item(self, item, *args, **kwargs):
            return item * 2
    
    with StatefulPoolType() as pool:
        yield pool

def test_imap(pool):
    results = pool.imap(MyState().process_item, range(10), chunksize=2)
    assert list(results) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPoolType_imap_0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_edge_case.py:3:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_edge_case.py:16:24: E0602: Undefined variable 'MyState' (undefined-variable)


"""