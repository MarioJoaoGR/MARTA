
import pytest
from pathlib import Path
import multiprocessing
import logging
from unittest.mock import patch, MagicMock
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def setup_logger():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger, handler

def test_invalid_inputs(setup_logger):
    logger, handler = setup_logger
    
    # Test invalid path type
    with pytest.raises(TypeError):
        MultiprocessingFileHandler(12345)  # Invalid path type

    # Test invalid mode type
    with pytest.raises(TypeError):
        MultiprocessingFileHandler(Path("logs/app.log"), mode=12345)  # Invalid mode type

    # Test non-existent directory for the log file
    non_existent_dir = Path("/nonexistent/directory/app.log")
    with pytest.raises(FileNotFoundError):
        MultiprocessingFileHandler(non_existent_dir)
