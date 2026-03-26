
import pytest
from unittest.mock import patch, MagicMock
import logging
import multiprocessing as mp
from pathlib import Path

# Assuming the module is named 'flutes' and contains the MultiprocessingFileHandler class
from flutes.log import MultiprocessingFileHandler

@pytest.fixture
def setup_logger():
    logger = logging.getLogger('test_logger')
    handler = MultiprocessingFileHandler(Path('test_logfile.log'))
    logger.addHandler(handler)
    return logger, handler

def test_setFormatter(setup_logger):
    logger, handler = setup_logger
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Test the setFormatter method
    handler.setFormatter(formatter)
    assert isinstance(handler._handler.formatter, type(formatter))
