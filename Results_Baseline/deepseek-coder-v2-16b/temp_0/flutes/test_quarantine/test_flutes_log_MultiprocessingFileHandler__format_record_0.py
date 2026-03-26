
# Module: flutes.log
import pytest
from logging import getLogger, DEBUG
from pathlib import Path
import multiprocessing as mp
import threading
from flutes.log import MultiprocessingFileHandler  # Replace 'flutes.log' with the actual module name where the handler is defined
import logging

def test_multiprocessingfilehandler_init():
    log_path = Path("logs/test.log")
    handler = MultiprocessingFileHandler(log_path)
    assert isinstance(handler._handler, logging.FileHandler), "Expected _handler to be an instance of logging.FileHandler"