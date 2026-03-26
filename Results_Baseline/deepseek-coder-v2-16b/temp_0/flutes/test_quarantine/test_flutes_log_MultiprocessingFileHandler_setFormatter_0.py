
import pytest
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler  # Replace 'your_module' with the actual module name where the handler is defined

# Test initialization of MultiprocessingFileHandler
def test_multiprocessingfilehandler_initialization():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    
    assert isinstance(handler, MultiprocessingFileHandler), "Handler should be an instance of MultiprocessingFileHandler"
    assert isinstance(handler._handler, logging.FileHandler), "Handler's internal handler should be a logging.FileHandler"