
import io
from flutes.io import _ProgressBufferedReader, BarFn
import os
import pytest

@pytest.fixture
def setup_reader():
    raw = io.BytesIO(b'some data')
    bar_fn = BarFn()
    reader = _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)
    return reader

def test_valid_input(setup_reader):
    reader = setup_reader
    assert isinstance(reader, _ProgressBufferedReader)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_io__ProgressBufferedReader___exit___0_test_valid_input
flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___0_test_valid_input.py:10:13: E0110: Abstract class 'Callable' with abstract methods instantiated (abstract-class-instantiated)

"""