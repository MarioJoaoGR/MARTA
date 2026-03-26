
import pytest
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler
import multiprocessing
import threading

@pytest.fixture(scope="module")
def logger():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    yield logger
    
    # Teardown: close the logger and remove the handler
    for handler in logger.handlers:
        logger.removeHandler(handler)
    handler.close()

def worker(logger, num):
    logger.debug(f"Worker {num} is working!")

def test_edge_cases(logger):
    # Create multiple processes to log messages
    processes = [multiprocessing.Process(target=worker, args=(logger, i)) for i in range(5)]
    
    # Start all processes
    for p in processes:
        p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()
