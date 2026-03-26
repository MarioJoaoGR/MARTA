
import pytest
from flutes.multiproc import StatefulPoolType
from multiprocessing import PoolState

class DummyState(PoolState):
    def process_item(self, item):
        return item

def test_invalid_inputs():
    with pytest.raises(TypeError):
        pool = StatefulPoolType(DummyState)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_StatefulPoolType_gather_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_gather_0_test_invalid_inputs.py:4:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)


"""