
import multiprocessing
from pathlib import Path
import logging
import flutes.log  # Assuming the log module is in this namespace
from flutes.log import MultiprocessingFileHandler

def worker(queue):
    logger = logging.getLogger(__name__)
    queue_handler = logging.handlers.QueueHandler(queue)
    logger.addHandler(queue_handler)
    logger.setLevel(logging.DEBUG)
    for i in range(5):
        logger.debug(f"Worker {i} is working!")

@pytest.mark.parametrize("num_workers", [1, 2, 3])
def test_multiprocessing_logging(setup_logger, num_workers):
    logger, handler = setup_logger
    queue = multiprocessing.Queue()

    processes = []
    for _ in range(num_workers):
        p = multiprocessing.Process(target=worker, args=(queue,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    # Check the log file content
    with open("logs/app.log", "r") as f:
        logs = f.readlines()

    assert len(logs) == num_workers * 5, f"Expected {num_workers * 5} messages, but got {len(logs)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_receive_0_test_edge_case
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_edge_case.py:16:1: E0602: Undefined variable 'pytest' (undefined-variable)


"""