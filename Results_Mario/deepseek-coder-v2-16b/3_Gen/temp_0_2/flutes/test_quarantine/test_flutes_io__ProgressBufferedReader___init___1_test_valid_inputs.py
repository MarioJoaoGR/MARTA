
import io
import os
from unittest import mock
import pytest
from flutes.io import _ProgressBufferedReader, BarFn

@pytest.fixture
def setup_reader():
    raw = io.BytesIO(b'some data')
    bar_fn = mock.MagicMock()
    return _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)

def test_valid_inputs(setup_reader):
    reader = setup_reader
    assert isinstance(reader._read_bytes, int)
    assert isinstance(reader.progress_bar, BarFn)
    file_size = os.fstat(reader._raw.fileno()).st_size
    assert reader.progress_bar.total == file_size

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

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___init___1_test_valid_inputs.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_valid_inputs ______________________

    @pytest.fixture
    def setup_reader():
        raw = io.BytesIO(b'some data')
        bar_fn = mock.MagicMock()
>       return _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___init___1_test_valid_inputs.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7fb2194db290>
buffer_size = 4096

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___init___1_test_valid_inputs.py::test_valid_inputs
=============================== 1 error in 0.10s ===============================
"""