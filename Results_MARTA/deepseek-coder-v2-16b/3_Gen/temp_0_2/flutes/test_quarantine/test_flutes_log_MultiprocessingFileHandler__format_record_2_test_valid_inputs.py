
import multiprocessing
import logging
from pathlib import Path
from flutes.log import MultiprocessingFileHandler

def test_valid_inputs():
    log_path = Path('test_logfile.log')
    
    # Set up logger
    logger = logging.getLogger(__name__)
    handler = MultiprocessingFileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    
    # Define a function to be run by multiple processes
    def worker_function():
        for i in range(5):
            logger.info("Log message number %s", i)
    
    if __name__ == "__main__":
        # Create and start multiple processes
        processes = [multiprocessing.Process(target=worker_function) for _ in range(3)]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
    
    # Read the log file to verify that messages were logged correctly
    with open(log_path, 'r') as f:
        logs = f.readlines()
    
    assert len(logs) == 15  # Each process logs 5 messages

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_2_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        log_path = Path('test_logfile.log')
    
        # Set up logger
        logger = logging.getLogger(__name__)
        handler = MultiprocessingFileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    
        # Define a function to be run by multiple processes
        def worker_function():
            for i in range(5):
                logger.info("Log message number %s", i)
    
        if __name__ == "__main__":
            # Create and start multiple processes
            processes = [multiprocessing.Process(target=worker_function) for _ in range(3)]
            for p in processes:
                p.start()
            for p in processes:
                p.join()
    
        # Read the log file to verify that messages were logged correctly
        with open(log_path, 'r') as f:
            logs = f.readlines()
    
>       assert len(logs) == 15  # Each process logs 5 messages
E       AssertionError: assert 1 == 15
E        +  where 1 = len(['Test log message\n'])

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_2_test_valid_inputs.py:35: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_2_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.12s ===============================
"""