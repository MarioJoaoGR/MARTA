
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler

def test_multiprocessing_logger():
    logger = logging.getLogger(__name__)
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    def worker(num):
        logger.debug(f"Worker {num} is working!")

    processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    # Read the log file to check if logs are written correctly
    with open("logs/app.log", "r") as f:
        logs = f.readlines()

    assert len(logs) == 5, f"Expected 5 log entries but got {len(logs)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_setFormatter_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_________________________ test_multiprocessing_logger __________________________

    def test_multiprocessing_logger():
        logger = logging.getLogger(__name__)
        log_path = Path("logs/app.log")
        handler = MultiprocessingFileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    
        def worker(num):
            logger.debug(f"Worker {num} is working!")
    
        processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
    
        # Read the log file to check if logs are written correctly
        with open("logs/app.log", "r") as f:
            logs = f.readlines()
    
>       assert len(logs) == 5, f"Expected 5 log entries but got {len(logs)}"
E       AssertionError: Expected 5 log entries but got 15
E       assert 15 == 5
E        +  where 15 = len(['Worker 0 is working!\n', 'Worker 1 is working!\n', 'Worker 2 is working!\n', 'Worker 3 is working!\n', 'Worker 4 is working!\n', 'Worker 0 is working!\n', ...])

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_setFormatter_0_test_edge_case.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_setFormatter_0_test_edge_case.py::test_multiprocessing_logger
============================== 1 failed in 0.11s ===============================
"""