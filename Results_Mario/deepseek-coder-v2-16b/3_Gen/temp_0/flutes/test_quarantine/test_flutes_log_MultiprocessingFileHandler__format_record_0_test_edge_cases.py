
import pytest
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler  # Assuming this is the correct module name

def worker(num):
    logger = logging.getLogger(__name__)
    logger.debug(f"Worker {num} is working!")

@pytest.fixture(scope="module")
def setup_logger():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    yield logger, handler
    # Teardown if necessary

def test_edge_cases(setup_logger):
    logger, handler = setup_logger
    processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
