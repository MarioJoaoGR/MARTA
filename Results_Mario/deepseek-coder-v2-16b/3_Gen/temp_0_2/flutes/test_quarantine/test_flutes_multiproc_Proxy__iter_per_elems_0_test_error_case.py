
import pytest
from flutes.multiproc import Proxy
from multiprocessing import Queue
from typing import Iterable, Iterator, TypeVar

T = TypeVar('T')

@pytest.fixture
def setup_proxy():
    queue = Queue()
    return Proxy(queue)

def test_iter_per_elems_error_case(setup_proxy):
    proxy = setup_proxy
    iterable = range(10)
    update_frequency = 3
    
    with pytest.raises(NotImplementedError):
        list(proxy._iter_per_elems(iterable, update_frequency))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy__iter_per_elems_0_test_error_case
flutes/Test4DT_tests/test_flutes_multiproc_Proxy__iter_per_elems_0_test_error_case.py:3:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""