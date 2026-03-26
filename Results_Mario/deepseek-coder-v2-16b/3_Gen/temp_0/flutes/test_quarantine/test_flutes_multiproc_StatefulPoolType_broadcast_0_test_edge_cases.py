
import pytest
from multiprocessing_stateful import safe_pool
import os

class MyState(PoolState):
    def __init__(self):
        self.data = {}

    def process_item(self, item):
        return item * 2

def test_broadcast():
    pool = safe_pool(MyState)
    results = pool.broadcast(MyState().process_item, args=(10,), kwds={'key': 'value'})
    assert isinstance(results, list)
    assert all(isinstance(result, int) for result in results)
    assert all(result == item * 2 for item, result in zip([10]*len(results), results))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPoolType_broadcast_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_broadcast_0_test_edge_cases.py:3:0: E0401: Unable to import 'multiprocessing_stateful' (import-error)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_broadcast_0_test_edge_cases.py:6:14: E0602: Undefined variable 'PoolState' (undefined-variable)


"""