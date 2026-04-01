
import pytest
from unittest.mock import patch, MagicMock
from flutes.log import get_worker_id

@pytest.mark.parametrize("proc_name, expected", [
    ("PoolWorker-123", 123),
    ("OtherProcessName-456", 456),
    ("PoolWorker", None),
    ("PoolWorker-abc", None),
    (None, None)
])
@patch('flutes.log.mp')
def test_get_worker_id(mock_mp, proc_name, expected):
    mock_proc = MagicMock()
    mock_proc.name = proc_name
    mock_mp.current_process.return_value = mock_proc
    
    assert get_worker_id() == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_valid_input.py . [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_________________ test_get_worker_id[OtherProcessName-456-456] _________________

mock_mp = <MagicMock name='mp' id='140061699897680'>
proc_name = 'OtherProcessName-456', expected = 456

    @pytest.mark.parametrize("proc_name, expected", [
        ("PoolWorker-123", 123),
        ("OtherProcessName-456", 456),
        ("PoolWorker", None),
        ("PoolWorker-abc", None),
        (None, None)
    ])
    @patch('flutes.log.mp')
    def test_get_worker_id(mock_mp, proc_name, expected):
        mock_proc = MagicMock()
        mock_proc.name = proc_name
        mock_mp.current_process.return_value = mock_proc
    
>       assert get_worker_id() == expected
E       assert None == 456
E        +  where None = get_worker_id()

flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_valid_input.py:19: AssertionError
_____________________ test_get_worker_id[PoolWorker-None] ______________________

mock_mp = <MagicMock name='mp' id='140061699794064'>, proc_name = 'PoolWorker'
expected = None

    @pytest.mark.parametrize("proc_name, expected", [
        ("PoolWorker-123", 123),
        ("OtherProcessName-456", 456),
        ("PoolWorker", None),
        ("PoolWorker-abc", None),
        (None, None)
    ])
    @patch('flutes.log.mp')
    def test_get_worker_id(mock_mp, proc_name, expected):
        mock_proc = MagicMock()
        mock_proc.name = proc_name
        mock_mp.current_process.return_value = mock_proc
    
>       assert get_worker_id() == expected

flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_valid_input.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def get_worker_id() -> Optional[int]:
        r"""Return the ID of the pool worker process, or ``None`` if the current process is not a pool worker."""
        proc_name = mp.current_process().name
        if "PoolWorker" in proc_name:
>           worker_id = int(proc_name[(proc_name.find('-') + 1):])
E           ValueError: invalid literal for int() with base 10: 'PoolWorker'

flutes/flutes/log.py:29: ValueError
___________________ test_get_worker_id[PoolWorker-abc-None] ____________________

mock_mp = <MagicMock name='mp' id='140061700436240'>
proc_name = 'PoolWorker-abc', expected = None

    @pytest.mark.parametrize("proc_name, expected", [
        ("PoolWorker-123", 123),
        ("OtherProcessName-456", 456),
        ("PoolWorker", None),
        ("PoolWorker-abc", None),
        (None, None)
    ])
    @patch('flutes.log.mp')
    def test_get_worker_id(mock_mp, proc_name, expected):
        mock_proc = MagicMock()
        mock_proc.name = proc_name
        mock_mp.current_process.return_value = mock_proc
    
>       assert get_worker_id() == expected

flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_valid_input.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def get_worker_id() -> Optional[int]:
        r"""Return the ID of the pool worker process, or ``None`` if the current process is not a pool worker."""
        proc_name = mp.current_process().name
        if "PoolWorker" in proc_name:
>           worker_id = int(proc_name[(proc_name.find('-') + 1):])
E           ValueError: invalid literal for int() with base 10: 'abc'

flutes/flutes/log.py:29: ValueError
________________________ test_get_worker_id[None-None] _________________________

mock_mp = <MagicMock name='mp' id='140061700578576'>, proc_name = None
expected = None

    @pytest.mark.parametrize("proc_name, expected", [
        ("PoolWorker-123", 123),
        ("OtherProcessName-456", 456),
        ("PoolWorker", None),
        ("PoolWorker-abc", None),
        (None, None)
    ])
    @patch('flutes.log.mp')
    def test_get_worker_id(mock_mp, proc_name, expected):
        mock_proc = MagicMock()
        mock_proc.name = proc_name
        mock_mp.current_process.return_value = mock_proc
    
>       assert get_worker_id() == expected

flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_valid_input.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def get_worker_id() -> Optional[int]:
        r"""Return the ID of the pool worker process, or ``None`` if the current process is not a pool worker."""
        proc_name = mp.current_process().name
>       if "PoolWorker" in proc_name:
E       TypeError: argument of type 'NoneType' is not iterable

flutes/flutes/log.py:28: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_valid_input.py::test_get_worker_id[OtherProcessName-456-456]
FAILED flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_valid_input.py::test_get_worker_id[PoolWorker-None]
FAILED flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_valid_input.py::test_get_worker_id[PoolWorker-abc-None]
FAILED flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_valid_input.py::test_get_worker_id[None-None]
========================= 4 failed, 1 passed in 0.12s ==========================
"""