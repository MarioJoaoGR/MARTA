
import io
from unittest.mock import MagicMock, patch
import pytest
from flutes.io import _ProgressBufferedReader

@pytest.fixture
def mock_progress_bar():
    pb = MagicMock()
    return pb

@pytest.fixture
def setup_reader(mock_progress_bar):
    raw = io.BytesIO(b'some data')
    reader = _ProgressBufferedReader(raw, bar_fn=lambda total: mock_progress_bar)
    return reader, mock_progress_bar

def test_exit_context_manager(setup_reader):
    reader, mock_progress_bar = setup_reader
    
    with patch('flutes.io._ProgressBufferedReader.__exit__', return_value=False):
        assert reader.__exit__(None, None, None) is False
        mock_progress_bar.__exit__.assert_called_once()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___0_test_edge_case.py E [100%]

==================================== ERRORS ====================================
_________________ ERROR at setup of test_exit_context_manager __________________

mock_progress_bar = <MagicMock id='139820771410640'>

    @pytest.fixture
    def setup_reader(mock_progress_bar):
        raw = io.BytesIO(b'some data')
>       reader = _ProgressBufferedReader(raw, bar_fn=lambda total: mock_progress_bar)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___0_test_edge_case.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>, raw = <_io.BytesIO object at 0x7f2a8f68bab0>
buffer_size = 8192

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
>       file_size = os.fstat(raw.fileno()).st_size
E       io.UnsupportedOperation: fileno

flutes/flutes/io.py:55: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___0_test_edge_case.py::test_exit_context_manager
=============================== 1 error in 0.08s ===============================

"""