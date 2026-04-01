
import logging
import multiprocessing as mp
import threading
from pathlib import Path
import pytest
from unittest.mock import MagicMock, patch

# Assuming the MultiprocessingFileHandler is defined in 'flutes.log' module
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def setup_logger():
    # Create a logger instance
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create an instance of MultiprocessingFileHandler with a temporary log file path
    handler = MultiprocessingFileHandler(Path("test_logfile.log"))
    logger.addHandler(handler)
    return handler, logger

def test_valid_input(setup_logger):
    handler, logger = setup_logger
    
    # Create a mock logging record with valid data
    record = logging.LogRecord(
        name="test", 
        level=logging.INFO, 
        pathname="test_path", 
        lineno=10, 
        msg="Test message", 
        args=(), 
        exc_info=None
    )
    
    # Patch the emit method to capture the output and check if it was called correctly
    with patch.object(handler, 'emit') as mock_emit:
        logger.handle(record)
        mock_emit.assert_called_once_with(record)
