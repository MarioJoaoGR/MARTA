
import pytest
from flutes.multiproc import Proxy  # Correctly importing from the module
import multiprocessing as mp

@pytest.fixture
def setup_proxy():
    queue = mp.Queue()
    return Proxy(queue)

def test_update_progress(setup_proxy):
    proxy = setup_proxy
    initial_count = 0
    expected_count = 10
    postfix = {"task": "running"}
    
    # Initial state check
    assert proxy.queue.qsize() == initial_count, f"Expected queue size to be {initial_count}, but got {proxy.queue.qsize()}"
    
    # Update progress
    proxy.update(n=expected_count, postfix=postfix)
    
    # Check if the update was successful
    assert proxy.queue.qsize() == expected_count, f"Expected queue size to be {expected_count}, but got {proxy.queue.qsize()}"

def test_update_with_postfix(setup_proxy):
    proxy = setup_proxy
    initial_count = 0
    postfix_value = {"task": "running"}
    
    # Initial state check
    assert proxy.queue.qsize() == initial_count, f"Expected queue size to be {initial_count}, but got {proxy.queue.qsize()}"
    
    # Update progress with postfix
    proxy.update(n=10, postfix=postfix_value)
    
    # Check if the update was successful
    assert proxy.queue.qsize() == 1, f"Expected queue size to be {1}, but got {proxy.queue.qsize()}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy_update_0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_Proxy_update_0_test_edge_case.py:3:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""