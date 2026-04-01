
import pytest
from pathlib import Path
import multiprocessing
import logging
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def setup_logger():
    log_path = Path("test_logs.log")
    handler = MultiprocessingFileHandler(log_path, mode='a')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    yield logger
    # Clean up the log file after the test
    if log_path.exists():
        log_path.unlink()

def worker_function(logger):
    for i in range(5):
        logger.info("Log message number %s", i)

def test_multiprocessing_logging(setup_logger):
    logger = setup_logger
    processes = [multiprocessing.Process(target=worker_function, args=(logger,)) for _ in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    # Check the log file content
    with open("test_logs.log", "r") as f:
        logs = f.readlines()
    
    assert len(logs) == 15, "Expected 15 log messages but got {}".format(len(logs))
