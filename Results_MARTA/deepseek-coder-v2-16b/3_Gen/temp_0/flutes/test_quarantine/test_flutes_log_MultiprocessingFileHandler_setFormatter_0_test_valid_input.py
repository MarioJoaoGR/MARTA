
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler

def worker(num):
    logger.debug(f"Worker {num} is working!")

if __name__ == "__main__":
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    
    # Set up the logger with the multiprocessing file handler
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_setFormatter_0_test_valid_input
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_setFormatter_0_test_valid_input.py:8:4: E0606: Possibly using variable 'logger' before assignment (possibly-used-before-assignment)


"""