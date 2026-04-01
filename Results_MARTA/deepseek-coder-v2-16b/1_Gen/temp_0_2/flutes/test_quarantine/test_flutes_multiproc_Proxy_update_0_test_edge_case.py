
import pytest
from flutes.multiproc import Proxy, UpdateEvent
import multiprocessing as mp

@pytest.fixture
def setup_proxy():
    queue = mp.Queue()
    return Proxy(queue)

def test_update_progress(setup_proxy):
    proxy = setup_proxy
    # Test updating progress without postfix
    proxy.update(n=10)
    event = proxy.queue.get()
    assert isinstance(event, UpdateEvent)
    assert event.increment == 10
    assert event.postfix is None

    # Test updating progress with postfix
    proxy.update(n=5, postfix={'unit': 'files'})
    event = proxy.queue.get()
    assert isinstance(event, UpdateEvent)
    assert event.increment == 5
    assert event.postfix == {'unit': 'files'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy_update_0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_Proxy_update_0_test_edge_case.py:3:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""