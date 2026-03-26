
import pytest
from flutes.multiproc import Proxy
import multiprocessing as mp
from typing import Iterable, Iterator, TypeVar

T = TypeVar('T')

@pytest.fixture
def setup_proxy():
    queue = mp.Queue()
    return Proxy(queue)

def test_invalid_input_length_zero(setup_proxy):
    with pytest.raises(ValueError):
        list(setup_proxy._iter_per_percentage([1, 2, 3], length=0, update_frequency=0.1))

def test_invalid_input_update_frequency_negative(setup_proxy):
    with pytest.raises(ValueError):
        list(setup_proxy._iter_per_percentage([1, 2, 3], length=3, update_frequency=-0.1))

def test_invalid_input_update_frequency_zero(setup_proxy):
    with pytest.raises(ValueError):
        list(setup_proxy._iter_per_percentage([1, 2, 3], length=3, update_frequency=0))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy__iter_per_percentage_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_Proxy__iter_per_percentage_0_test_invalid_input.py:3:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""