
import io
from flutes.io import _ProgressBufferedReader
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def setup_reader():
    raw = io.BytesIO(b'some data')
    bar_fn = MagicMock()
    reader = _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)
    return reader, raw, bar_fn

def test_valid_inputs(setup_reader):
    reader, raw, bar_fn = setup_reader
    assert isinstance(reader, _ProgressBufferedReader)
    assert reader.buffer_size == 4096
    assert reader._raw is raw
    assert reader.progress_bar is bar_fn

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___enter___0_test_valid_inputs.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_valid_inputs ______________________

    @pytest.fixture
    def setup_reader():
        raw = io.BytesIO(b'some data')
        bar_fn = MagicMock()
>       reader = _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___enter___0_test_valid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7f851e2b0950>
buffer_size = 4096

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___enter___0_test_valid_inputs.py::test_valid_inputs
=============================== 1 error in 0.12s ===============================
"""