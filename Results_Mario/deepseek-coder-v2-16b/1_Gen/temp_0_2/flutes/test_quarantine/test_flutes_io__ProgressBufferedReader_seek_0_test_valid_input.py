
import io
import os
from flutes.io import _ProgressBufferedReader, BarFn
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def setup_reader():
    raw = io.BytesIO(b'test data')
    bar_fn = lambda total: MagicMock()  # Mock the progress bar function
    reader = _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)
    return reader

def test_seek_valid_input(setup_reader):
    reader = setup_reader
    initial_position = reader.tell()
    assert initial_position == 0
    
    new_position = reader.seek(10, io.SEEK_SET)
    assert new_position == 10
    assert reader.tell() == 10
    
    new_position = reader.seek(-5, io.SEEK_CUR)
    assert new_position == 5
    assert reader.tell() == 5
    
    new_position = reader.seek(20, io.SEEK_END)
    assert new_position == len(reader._buffer) + len(b'test data')
    assert reader.tell() == len(reader._buffer) + len(b'test data')

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

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_seek_0_test_valid_input.py E [100%]

==================================== ERRORS ====================================
___________________ ERROR at setup of test_seek_valid_input ____________________

    @pytest.fixture
    def setup_reader():
        raw = io.BytesIO(b'test data')
        bar_fn = lambda total: MagicMock()  # Mock the progress bar function
>       reader = _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_seek_0_test_valid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7f953b578810>
buffer_size = 4096

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_seek_0_test_valid_input.py::test_seek_valid_input
=============================== 1 error in 0.09s ===============================
"""