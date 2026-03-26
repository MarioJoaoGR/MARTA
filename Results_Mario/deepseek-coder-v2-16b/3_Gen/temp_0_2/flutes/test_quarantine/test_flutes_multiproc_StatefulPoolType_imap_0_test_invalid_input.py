
import pytest
from multiprocessing import PoolState
from flutes.multiproc import StatefulPoolType

@pytest.fixture
def stateful_pool():
    class MyInvalidState(PoolState):
        def process_item(self, item, *args, **kwargs):
            return item * 2

    pool = StatefulPoolType()
    yield pool
    pool.terminate()

def test_invalid_input(stateful_pool):
    with pytest.raises(TypeError):
        results = stateful_pool.imap(MyInvalidState().process_item, range(10), chunksize=2)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPoolType_imap_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_invalid_input.py:3:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_invalid_input.py:18:37: E0602: Undefined variable 'MyInvalidState' (undefined-variable)


"""