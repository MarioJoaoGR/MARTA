
import multiprocessing
from logging import getLogger, FileHandler, Formatter
from pathlib import Path
from flutes.log import MultiprocessingFileHandler

def test_logger_logs_from_multiple_processes(tmpdir):
    log_path = Path(tmpdir) / "test_logfile.log"
    logger = getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    handler = MultiprocessingFileHandler(log_path, mode='a')
    formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    def worker_function():
        for i in range(5):
            logger.info("Log message number %s", i)
    
    processes = [multiprocessing.Process(target=worker_function) for _ in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    with open(log_path, 'r') as logfile:
        logs = logfile.readlines()
    
    assert len(logs) == 15, f"Expected 15 log messages but got {len(logs)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler__format_record_2_test_edge_cases
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_2_test_edge_cases.py:10:20: E0602: Undefined variable 'logging' (undefined-variable)


"""