
import multiprocessing
from logging import getLogger, FileHandler, Formatter
from pathlib import Path
from custom_module import MultiprocessingFileHandler

def test_valid_case():
    # Set up logger
    logger = getLogger(__name__)
    log_path = Path('logs/app.log')
    handler = MultiprocessingFileHandler(log_path, mode='a')
    formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # Example logging from a process
    def worker_function():
        for i in range(5):
            logger.info("Log message number %s", i)

    if __name__ == "__main__":
        processes = [multiprocessing.Process(target=worker_function) for _ in range(3)]
        for p in processes:
            p.start()
        for p in processes:
            p.join()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler__format_record_0_test_valid_case
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_0_test_valid_case.py:5:0: E0401: Unable to import 'custom_module' (import-error)
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler__format_record_0_test_valid_case.py:15:20: E0602: Undefined variable 'logging' (undefined-variable)


"""