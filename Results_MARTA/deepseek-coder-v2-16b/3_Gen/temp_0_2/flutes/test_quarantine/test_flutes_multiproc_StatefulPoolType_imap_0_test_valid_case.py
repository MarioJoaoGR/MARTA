
import pytest
from multiprocessing import PoolState
from flutes.multiproc import StatefulPoolType

def test_valid_case():
    class MyState(PoolState):
        def process_item(self, item, *args, **kwargs):
            return item * 2

    with StatefulPoolType() as pool:
        results = pool.imap(MyState().process_item, range(10), chunksize=2)
    
    expected_results = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    assert list(results) == expected_results

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPoolType_imap_0_test_valid_case
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_valid_case.py:3:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_0_test_valid_case.py:12:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""