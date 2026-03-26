
import pytest
from flutes.multiproc import Proxy
import multiprocessing as mp
from typing import Union, Literal
from tqdm import tqdm

@pytest.mark.parametrize("iterable, update_frequency", [
    (None, 1),
    ([1, 2, 3], 0.5),
    ((i for i in range(10)), 1)
])
def test_new_method(iterable: Union[list, tuple, Literal[None]], update_frequency: Union[int, float]):
    queue = mp.Queue()
    proxy = Proxy(queue)
    
    # Call the new method and check if it returns a tqdm instance
    progress_bar = proxy.new(iterable=iterable, update_frequency=update_frequency)
    assert isinstance(progress_bar, tqdm), "Expected a tqdm instance"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy_new_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_Proxy_new_0_test_invalid_inputs.py:3:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""