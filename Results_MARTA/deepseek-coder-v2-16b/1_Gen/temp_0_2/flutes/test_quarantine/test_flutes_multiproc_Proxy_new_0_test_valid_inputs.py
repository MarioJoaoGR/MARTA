
import pytest
from flutes.multiproc import Proxy
import multiprocessing as mp
from typing import Union, Literal
from tqdm import tqdm

@pytest.fixture
def setup_proxy():
    queue = mp.Queue()
    return Proxy(queue)

def test_new_method(setup_proxy):
    proxy = setup_proxy
    iterable = [1, 2, 3, 4, 5]
    update_frequency = 0.5
    kwargs = {}
    
    progress_bar = proxy.new(iterable, update_frequency, **kwargs)
    
    assert isinstance(progress_bar, tqdm), "Expected a tqdm instance"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy_new_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_Proxy_new_0_test_valid_inputs.py:3:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""