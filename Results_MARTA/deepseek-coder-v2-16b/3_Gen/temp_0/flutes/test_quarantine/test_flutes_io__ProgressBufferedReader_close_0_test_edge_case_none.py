
import io
from unittest.mock import MagicMock
import pytest
from flutes.io import _ProgressBufferedReader

def test_close():
    # Create a mock raw IO base
    raw = io.BytesIO(b'some data')
    
    # Create a mock progress bar function
    bar_fn = MagicMock()
    
    # Instantiate the ProgressBufferedReader with the mock raw and bar_fn
    reader = _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)
    
    # Call the close method
    reader.close()
    
    # Assert that the progress bar function was called to close
    bar_fn.assert_called_once()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_close_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
__________________________________ test_close __________________________________

    def test_close():
        # Create a mock raw IO base
        raw = io.BytesIO(b'some data')
    
        # Create a mock progress bar function
        bar_fn = MagicMock()
    
        # Instantiate the ProgressBufferedReader with the mock raw and bar_fn
>       reader = _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_close_0_test_edge_case_none.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7f6f7e28ab60>
buffer_size = 4096

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_close_0_test_edge_case_none.py::test_close
============================== 1 failed in 0.08s ===============================

"""