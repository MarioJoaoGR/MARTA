
import pytest
import multiprocessing
from pathlib import Path
import logging
from unittest.mock import patch
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def logger():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    yield logger
    # Clean up the logger after the test
    for h in logger.handlers:
        logger.removeHandler(h)

def worker(num, logger):
    while True:
        logger.debug(f"Debug message from process {num}")

@patch('multiprocessing.Process', autospec=True)
def test_valid_inputs(mock_process, logger):
    processes = [multiprocessing.Process(target=worker, args=(i, logger)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
