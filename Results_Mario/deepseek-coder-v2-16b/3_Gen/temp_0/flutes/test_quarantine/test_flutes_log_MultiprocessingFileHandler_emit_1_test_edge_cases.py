
import pytest
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler  # Assuming it's part of flutes.log module

def worker(num):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = MultiprocessingFileHandler(Path("logs/app.log"))
    logger.addHandler(handler)
    logger.debug(f"Worker {num} is working!")

def test_edge_cases():
    processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    # Add assertions to check the log file content if necessary
