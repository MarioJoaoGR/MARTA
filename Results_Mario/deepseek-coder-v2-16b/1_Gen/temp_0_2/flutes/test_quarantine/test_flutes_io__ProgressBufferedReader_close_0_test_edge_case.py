
import io
from unittest.mock import MagicMock
import pytest
from flutes.io import _ProgressBufferedReader

@pytest.fixture
def setup_progress_buffered_reader():
    raw = io.BytesIO(b"test data")
    bar_fn = MagicMock()
    return _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)

def test_close(setup_progress_buffered_reader):
    reader = setup_progress_buffered_reader
    reader.close()
    assert reader.progress_bar.close.called

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

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_close_0_test_edge_case.py E [100%]

==================================== ERRORS ====================================
_________________________ ERROR at setup of test_close _________________________

    @pytest.fixture
    def setup_progress_buffered_reader():
        raw = io.BytesIO(b"test data")
        bar_fn = MagicMock()
>       return _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_close_0_test_edge_case.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7fef469c85e0>
buffer_size = 4096

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_close_0_test_edge_case.py::test_close
=============================== 1 error in 0.10s ===============================
"""