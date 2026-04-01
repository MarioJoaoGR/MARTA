
import logging
import multiprocessing as mp
import threading
from pathlib import Path
import pytest
from unittest.mock import MagicMock, patch

# Assuming the MultiprocessingFileHandler is in a module named 'flutes.log'
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def setup_logger():
    # Create a logger instance
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create an instance of MultiprocessingFileHandler with a mock path
    handler = MultiprocessingFileHandler(Path("logfile.log"))

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger, handler

def test_valid_input(setup_logger):
    logger, handler = setup_logger
    
    # Create a mock log record with valid input
    record = logging.LogRecord(
        name="test", 
        level=logging.INFO, 
        pathname="logfile.log", 
        lineno=10, 
        msg="Test message", 
        args=(), 
        exc_info=None
    )
    
    # Use patch to mock the emit method of the handler
    with patch.object(handler, 'emit') as mock_emit:
        logger.handle(record)
        
        # Assert that the emit method was called with the correct record
        mock_emit.assert_called_once_with(record)
