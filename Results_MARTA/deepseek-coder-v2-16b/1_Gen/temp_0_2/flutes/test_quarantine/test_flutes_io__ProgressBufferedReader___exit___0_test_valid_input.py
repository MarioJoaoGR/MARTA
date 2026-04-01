
import io
from unittest.mock import MagicMock
import pytest
from flutes.io import _ProgressBufferedReader, BarFn

@pytest.fixture
def setup_reader():
    raw = io.BytesIO(b'test data')
    bar_fn = MagicMock(spec=BarFn)
    reader = _ProgressBufferedReader(raw, buffer_size=1024, bar_fn=bar_fn)
    return reader, bar_fn

def test_progress_tracking(setup_reader):
    reader, bar_fn = setup_reader
    
    # Read a chunk of data to trigger progress bar update
    assert reader.read(512) == b'test '
    bar_fn.update.assert_called_with(512)  # Check if the progress bar was updated with the correct amount of bytes read
    
    # Read more data
    assert reader.read(512) == b'data'
    bar_fn.update.assert_called_with(512)  # Check if the progress bar was updated again

def test_context_manager(setup_reader):
    reader, bar_fn = setup_reader
    
    with pytest.raises(Exception) as excinfo:
        with reader:
            raise Exception("Test exception")
    
    # Check if the progress bar was properly closed even though an exception occurred
    bar_fn.__exit__.assert_called()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___0_test_valid_input.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
___________________ ERROR at setup of test_progress_tracking ___________________

    @pytest.fixture
    def setup_reader():
        raw = io.BytesIO(b'test data')
        bar_fn = MagicMock(spec=BarFn)
>       reader = _ProgressBufferedReader(raw, buffer_size=1024, bar_fn=bar_fn)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___0_test_valid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7f879e9905e0>
buffer_size = 1024

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
____________________ ERROR at setup of test_context_manager ____________________

    @pytest.fixture
    def setup_reader():
        raw = io.BytesIO(b'test data')
        bar_fn = MagicMock(spec=BarFn)
>       reader = _ProgressBufferedReader(raw, buffer_size=1024, bar_fn=bar_fn)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___0_test_valid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7f879e9937e0>
buffer_size = 1024

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___0_test_valid_input.py::test_progress_tracking
ERROR flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___0_test_valid_input.py::test_context_manager
============================== 2 errors in 0.10s ===============================
"""