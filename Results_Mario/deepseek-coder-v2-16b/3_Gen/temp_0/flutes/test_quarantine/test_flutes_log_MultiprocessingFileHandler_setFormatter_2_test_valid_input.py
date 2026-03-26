
import multiprocessing
from pathlib import Path
import logging
from flutes.log import MultiprocessingFileHandler  # Replace 'flutes.log' with the actual module name where the handler is defined

def test_valid_input():
    log_path = Path("logs/app.log")
    handler = MultiprocessingFileHandler(log_path)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    # Now you can log messages in any process without worrying about thread safety or file access conflicts:
    def worker(num):
        logger.debug(f"Worker {num} is working!")
    
    processes = [multiprocessing.Process(target=worker, args=(i,)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
