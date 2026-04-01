
import io
import os
import pytest
from flutes.io import _ProgressBufferedReader, BarFn

def test_invalid_input():
    with pytest.raises(TypeError):
        # Passing an invalid type for bar_fn should raise a TypeError
        raw = io.BytesIO()
        with pytest.raises(TypeError):
            _ProgressBufferedReader(raw, buffer_size=4096, bar_fn="invalid_type")

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

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_close_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
            # Passing an invalid type for bar_fn should raise a TypeError
            raw = io.BytesIO()
            with pytest.raises(TypeError):
>               _ProgressBufferedReader(raw, buffer_size=4096, bar_fn="invalid_type")

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_close_0_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7f4fa6eec9a0>
buffer_size = 4096

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_close_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""