
import pytest
from flutes.multiproc import Proxy, Event
import multiprocessing as mp

@pytest.fixture
def setup_proxy():
    queue = mp.Queue()
    return Proxy(queue)

def test_proxy_init(setup_proxy):
    proxy = setup_proxy
    assert isinstance(proxy.queue, mp.Queue)
    assert issubclass(proxy.queue.__class__, mp.Queue)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy___init___0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_Proxy___init___0_test_edge_case.py:3:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)

"""