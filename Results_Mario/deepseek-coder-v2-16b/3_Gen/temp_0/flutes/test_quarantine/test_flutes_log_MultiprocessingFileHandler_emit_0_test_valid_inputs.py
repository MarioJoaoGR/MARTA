
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler  # Assuming this is the correct module name
import os
import pytest

def worker(num):
    logger = logging.getLogger(__name__)
    logger.debug(f"Worker {num} is working!")

@pytest.fixture
def setup_logger():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return (logger, handler)

def test_valid_inputs(setup_logger):
    logger, handler = setup_logger
    processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
    
    # Start all the processes
    for p in processes:
        p.start()
    
    # Wait for all the processes to complete
    for p in processes:
        p.join()
    
    # Check the log file content
    with open("logs/app.log", "r") as f:
        logs = f.readlines()
    
    assert len(logs) == 5, "Expected 5 log entries but got different number"
