
import pytest
from multiprocessing import Pool
from stateful_pool import State, StatefulPool

@pytest.fixture(scope="module")
def pool():
    class MyState(State):
        def process(self, data):
            return sum(data)

    pool = StatefulPool(Pool, MyState, ((), {}), args=(), kwargs={})
    yield pool
    # Teardown code if needed

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPool_broadcast_1_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool_broadcast_1_test_valid_inputs.py:4:0: E0401: Unable to import 'stateful_pool' (import-error)


"""