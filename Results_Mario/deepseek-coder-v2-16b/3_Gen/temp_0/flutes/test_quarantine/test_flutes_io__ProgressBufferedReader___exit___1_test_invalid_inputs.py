
import io
from unittest.mock import MagicMock, patch
import pytest
from flutes.io import _ProgressBufferedReader

@pytest.mark.parametrize("invalid_input", [None, 123, "string"])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError) as excinfo:
        reader = _ProgressBufferedReader(io.BytesIO(), bar_fn=invalid_input)
    assert "'bar_fn' is required" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___1_test_invalid_inputs.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_inputs[None] ___________________________

invalid_input = None

    @pytest.mark.parametrize("invalid_input", [None, 123, "string"])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError) as excinfo:
>           reader = _ProgressBufferedReader(io.BytesIO(), bar_fn=invalid_input)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___1_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7faf72dc5300>
buffer_size = 8192

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
___________________________ test_invalid_inputs[123] ___________________________

invalid_input = 123

    @pytest.mark.parametrize("invalid_input", [None, 123, "string"])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError) as excinfo:
>           reader = _ProgressBufferedReader(io.BytesIO(), bar_fn=invalid_input)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___1_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7faf72bf7470>
buffer_size = 8192

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
_________________________ test_invalid_inputs[string] __________________________

invalid_input = 'string'

    @pytest.mark.parametrize("invalid_input", [None, 123, "string"])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError) as excinfo:
>           reader = _ProgressBufferedReader(io.BytesIO(), bar_fn=invalid_input)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___1_test_invalid_inputs.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7faf72bf7380>
buffer_size = 8192

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___1_test_invalid_inputs.py::test_invalid_inputs[None]
FAILED flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___1_test_invalid_inputs.py::test_invalid_inputs[123]
FAILED flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___1_test_invalid_inputs.py::test_invalid_inputs[string]
============================== 3 failed in 0.13s ===============================
"""