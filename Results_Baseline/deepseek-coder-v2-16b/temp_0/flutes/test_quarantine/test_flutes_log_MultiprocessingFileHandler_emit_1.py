
import multiprocessing
from pathlib import Path
import logging
import pytest
from flutes.log import MultiprocessingFileHandler  # Replace 'your_module' with the actual module name where the handler is defined

@pytest.fixture(scope="module")
def logger():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    yield logger
    # Clean up the log file after tests are done
    with open("logs/app.log", "w") as f:
        f.truncate(0)

def worker(logger, num):
    logger.debug(f"Worker {num} is working!")

def test_basic_usage(logger):
    processes = [multiprocessing.Process(target=worker, args=(logger, i)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    with open("logs/app.log", "r") as f:
        logs = f.readlines()
        assert len(logs) == 5, f"Expected 5 log messages but got {len(logs)}"
        for i in range(5):
            assert f"Worker {i} is working!" in logs[i], f"Log message from worker {i} not found"

def test_custom_mode(logger):
    with open("logs/app.log", "w") as f:
        f.truncate(0)  # Ensure the log file is empty before starting new tests
    
    processes = [multiprocessing.Process(target=worker, args=(logger, i)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    with open("logs/app.log", "r") as f:
        logs = f.readlines()