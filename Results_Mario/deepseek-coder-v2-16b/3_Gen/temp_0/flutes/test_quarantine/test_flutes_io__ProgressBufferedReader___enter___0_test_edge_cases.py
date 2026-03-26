
import io
from unittest.mock import MagicMock, patch
import pytest
from flutes.io import _ProgressBufferedReader

@pytest.fixture
def raw_io():
    return io.BytesIO(b'some data')

@pytest.fixture
def bar_fn():
    bar = MagicMock()
    bar.return_value = bar
    return bar

def test_progress_buffered_reader_enter(raw_io, bar_fn):
    with patch('os.fstat', return_value=MagicMock(st_size=len(raw_io.getvalue()))):
        reader = _ProgressBufferedReader(raw_io, buffer_size=4096, bar_fn=bar_fn)
        assert reader._read_bytes == 0
        with pytest.raises(StopIteration):
            next(reader)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___enter___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_____________________ test_progress_buffered_reader_enter ______________________

raw_io = <_io.BytesIO object at 0x7f68feb6ff60>
bar_fn = <MagicMock id='140088911063120'>

    def test_progress_buffered_reader_enter(raw_io, bar_fn):
        with patch('os.fstat', return_value=MagicMock(st_size=len(raw_io.getvalue()))):
>           reader = _ProgressBufferedReader(raw_io, buffer_size=4096, bar_fn=bar_fn)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___enter___0_test_edge_cases.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7f68feb6ff60>
buffer_size = 4096

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___enter___0_test_edge_cases.py::test_progress_buffered_reader_enter
============================== 1 failed in 0.12s ===============================
"""