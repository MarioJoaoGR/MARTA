
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler  # Assuming this is the correct module name

def worker(num):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = MultiprocessingFileHandler("logs/app.log")
    logger.addHandler(handler)
    logger.debug(f"Worker {num} is working!")

def test_valid_case():
    processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    log_file = Path("logs/app.log")
    assert log_file.exists(), "Log file does not exist"
    with open(log_file, 'r') as f:
        logs = f.readlines()
    assert len(logs) == 5, f"Expected 5 log entries but found {len(logs)}"

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
    
        log_file = Path("logs/app.log")
        assert log_file.exists(), "Log file does not exist"
        with open(log_file, 'r') as f:
            logs = f.readlines()
>       assert len(logs) == 5, f"Expected 5 log entries but found {len(logs)}"
E       AssertionError: Expected 5 log entries but found 1
E       assert 1 == 5
E        +  where 1 = len(['Test message with placeholder value\n'])

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_case.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_emit_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.10s ===============================
"""