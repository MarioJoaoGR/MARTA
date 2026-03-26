
import pytest
from multiprocessing import Queue
from flutes.multiproc import Proxy, Event

@pytest.fixture
def setup_proxy():
    queue = Queue()
    proxy = Proxy(queue)
    return proxy

def test_invalid_input(setup_proxy):
    proxy = setup_proxy
    
    with pytest.raises(TypeError):
        for item in proxy._iter_per_percentage("not an iterable", 10, 0.1):
            pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy__iter_per_percentage_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_Proxy__iter_per_percentage_0_test_invalid_input.py:4:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""