
import pytest
from logging import getLogger, DEBUG, FileHandler
from pathlib import Path
from multiprocessing import Process, Queue
import threading
import time

# Assuming the module is named 'flutes.log' and contains the MultiprocessingFileHandler class
from flutes.log import MultiprocessingFileHandler

def test_invalid_inputs():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    
    def worker(queue):
        logger.debug("Debug message from process")
        queue.put("logged")
    
    queue = Queue()
    p = Process(target=worker, args=(queue,))
    p.start()
    p.join()
    
    assert not queue.empty(), "Log message was expected but not found"
