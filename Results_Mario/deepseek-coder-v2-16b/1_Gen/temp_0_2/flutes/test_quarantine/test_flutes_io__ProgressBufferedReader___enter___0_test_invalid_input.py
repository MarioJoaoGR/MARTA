
import io
from flutes.io import _ProgressBufferedReader
import pytest
import os

@pytest.fixture
def setup_reader():
    raw = io.BytesIO(b'test data')
    progress_bar_fn = lambda total: None  # Mock progress bar function
    reader = _ProgressBufferedReader(raw, buffer_size=1024, bar_fn=progress_bar_fn)
    return reader

def test_invalid_input(setup_reader):
    with pytest.raises(io.UnsupportedOperation):
        setup_reader.__enter__()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___enter___0_test_invalid_input.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_invalid_input _____________________

    @pytest.fixture
    def setup_reader():
        raw = io.BytesIO(b'test data')
        progress_bar_fn = lambda total: None  # Mock progress bar function
>       reader = _ProgressBufferedReader(raw, buffer_size=1024, bar_fn=progress_bar_fn)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___enter___0_test_invalid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7f757d788ae0>
buffer_size = 1024

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___enter___0_test_invalid_input.py::test_invalid_input
=============================== 1 error in 0.10s ===============================
"""