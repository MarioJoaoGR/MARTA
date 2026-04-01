
import pytest
from unittest.mock import patch, MagicMock
from flutes.log import get_worker_id

@pytest.mark.parametrize("proc_name, expected", [
    ("PoolWorker-0", 0),
    ("PoolWorker-1", 1),
    ("OtherProcessName", None),
    (None, None)
])
def test_get_worker_id(proc_name, expected):
    with patch('flutes.log.mp') as mock_mp:
        mock_process = MagicMock()
        mock_process.name = proc_name
        mock_mp.current_process.return_value = mock_process

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
collected 4 items

flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_invalid_input.py . [ 25%]
..F                                                                      [100%]

=================================== FAILURES ===================================
________________________ test_get_worker_id[None-None] _________________________

proc_name = None, expected = None

    @pytest.mark.parametrize("proc_name, expected", [
        ("PoolWorker-0", 0),
        ("PoolWorker-1", 1),
        ("OtherProcessName", None),
        (None, None)
    ])
    def test_get_worker_id(proc_name, expected):
        with patch('flutes.log.mp') as mock_mp:
            mock_process = MagicMock()
            mock_process.name = proc_name
            mock_mp.current_process.return_value = mock_process
    
>           assert get_worker_id() == expected

flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_invalid_input.py:18: 
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
FAILED flutes/Test4DT_tests/test_flutes_log_get_worker_id_2_test_invalid_input.py::test_get_worker_id[None-None]
========================= 1 failed, 3 passed in 0.11s ==========================
"""