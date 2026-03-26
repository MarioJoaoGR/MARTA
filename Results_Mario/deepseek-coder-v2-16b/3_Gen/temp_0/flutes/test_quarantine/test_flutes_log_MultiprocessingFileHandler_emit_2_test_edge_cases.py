
import multiprocessing
from unittest.mock import patch
from flutes.log import MultiprocessingFileHandler
import logging

def worker(num):
    logger = logging.getLogger(__name__)
    handler = MultiprocessingFileHandler("logs/app.log")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.debug(f"Worker {num} is working!")

def test_edge_cases():
    with patch('flutes.log.MultiprocessingFileHandler.emit') as mock_emit:
        processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
    
    assert mock_emit.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_2_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        with patch('flutes.log.MultiprocessingFileHandler.emit') as mock_emit:
            processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
            for p in processes:
                p.start()
            for p in processes:
                p.join()
    
>       assert mock_emit.called
E       AssertionError: assert False
E        +  where False = <MagicMock name='emit' id='139845303400848'>.called

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_2_test_edge_cases.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_2_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.13s ===============================
"""