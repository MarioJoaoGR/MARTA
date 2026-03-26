
import pytest
from flutes.multiproc import Proxy
from multiprocessing import Queue
from typing import Iterable, Iterator, TypeVar

T = TypeVar('T')

@pytest.fixture
def proxy():
    queue = Queue()
    return Proxy(queue)

def test_iter_per_elems(proxy):
    iterable = [1, 2, 3, 4, 5]
    update_frequency = 2
    
    result = list(proxy._iter_per_elems(iterable, update_frequency))
    
    assert result == [1, 2, 3, 4, 5]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy__iter_per_elems_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_Proxy__iter_per_elems_0_test_valid_inputs.py:3:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""