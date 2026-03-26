
import pytest
from multiprocessing import Queue
from flutes.multiproc import Proxy, Event

@pytest.fixture
def setup_proxy():
    queue = Queue()
    proxy = Proxy(queue)
    return proxy

def test_valid_case(setup_proxy):
    proxy = setup_proxy
    iterable = [1, 2, 3, 4, 5]
    length = len(iterable)
    update_frequency = 0.1
    
    result = []
    for item in proxy._iter_per_percentage(iterable, length, update_frequency):
        result.append(item)
    
    assert result == iterable

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy__iter_per_percentage_0_test_valid_case
flutes/Test4DT_tests/test_flutes_multiproc_Proxy__iter_per_percentage_0_test_valid_case.py:4:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""