
import pytest
from multiprocessing import Pool
from flutes.multiproc import StatefulPool, MyState

@pytest.fixture
def setup_statefulpool():
    pool = StatefulPool(Pool, MyState, (1, 2), (), {})
    return pool

def test_edge_case(setup_statefulpool):
    pool = setup_statefulpool
    assert hasattr(pool, 'imap')
    assert hasattr(pool, 'map')
    assert hasattr(pool, 'apply')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPool___getattr___0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPool___getattr___0_test_edge_case.py:4:0: E0611: No name 'MyState' in module 'flutes.multiproc' (no-name-in-module)


"""