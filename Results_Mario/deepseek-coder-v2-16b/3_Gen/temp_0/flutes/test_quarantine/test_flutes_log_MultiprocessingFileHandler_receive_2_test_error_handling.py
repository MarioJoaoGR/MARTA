
import multiprocessing
from flutes.log import MultiprocessingFileHandler  # Assuming this is the correct module path
import logging

def worker(queue):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.QueueHandler(queue)
    logger.addHandler(handler)
    logger.debug("Worker message")  # Log a message to be captured in the test

@pytest.mark.parametrize("num_processes", [1, 2, 3])
def test_error_handling(setup_logger, num_processes, capsys):
    handler, logger = setup_logger
    queue = multiprocessing.Queue()
    
    processes = [multiprocessing.Process(target=worker, args=(queue,)) for _ in range(num_processes)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    # Capture the output to check if logs are correctly written
    captured = capsys.readouterr()
    assert "Worker message" in captured.out

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_receive_2_test_error_handling
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_2_test_error_handling.py:13:1: E0602: Undefined variable 'pytest' (undefined-variable)


"""