
import pytest
from unittest.mock import patch, MagicMock
from flutes.log import MultiprocessingFileHandler
import multiprocessing as mp
import logging
import threading
import sys
import traceback

@pytest.fixture(scope="module")
def setup_logger():
    logger = logging.getLogger("test_logger")
    handler = MultiprocessingFileHandler("logs/application.log", mode="a")
    logger.addHandler(handler)
    return logger, handler

def test_invalid_inputs(setup_logger):
    logger, handler = setup_logger
    
    # Test with None as path (should raise a TypeError)
    with pytest.raises(TypeError):
        MultiprocessingFileHandler(None)
        
    # Test with an integer as path (should raise a TypeError)
    with pytest.raises(TypeError):
        MultiprocessingFileHandler(12345)
        
    # Test with invalid mode (should raise a ValueError)
    with pytest.raises(ValueError):
        MultiprocessingFileHandler("logs/application.log", mode="invalid_mode")
