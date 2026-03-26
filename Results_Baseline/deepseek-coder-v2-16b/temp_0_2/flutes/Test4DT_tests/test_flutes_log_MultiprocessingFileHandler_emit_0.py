
import pytest
import multiprocessing
import threading
import logging
from pathlib import Path
import queue as mp_queue

# Import the function from the module
from flutes.log import MultiprocessingFileHandler

@pytest.fixture
def setup_logger():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    
    # Create an instance of the MultiprocessingFileHandler with default mode 'a'
    log_handler = MultiprocessingFileHandler(Path("logs/app.log"))
    
    # Add the handler to the logger
    logger.addHandler(log_handler)
    
    return logger, log_handler

def test_basic_initialization(setup_logger):
    logger, _ = setup_logger
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], MultiprocessingFileHandler)

def test_specifying_mode(tmp_path):
    log_file = tmp_path / "test.log"
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    
    # Create an instance of the MultiprocessingFileHandler for writing to 'test.log' in write mode "w"
    log_handler = MultiprocessingFileHandler(log_file, mode="w")
    
    # Add the handler to the logger
    logger.addHandler(log_handler)
    