
import pytest
from pathlib import Path
import logging
import multiprocessing
import threading
from unittest.mock import patch, MagicMock
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def setup_logger():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return handler, logger

def worker(num):
    logger = logging.getLogger(__name__)
    logger.debug(f"Worker {num} is working!")

@patch('flutes.log.mp', MagicMock())
def test_valid_inputs():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
