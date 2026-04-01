
import logging
import multiprocessing as mp
import threading
from pathlib import Path  # Importing Path from pathlib for type hinting

class MultiprocessingFileHandler(logging.Handler):
    """Class for handling multiprocessing logging to the same file using a queue.
    
    This class allows multiple processes to log messages to the same file by utilizing a shared queue. It is based on the provided example and credit from https://mattgathu.github.io/multiprocessing-logging-in-python/.
    
    Parameters:
        path (PathType): The file path where logs will be written.
        mode (str, optional): The mode in which to open the log file ('a' for append or 'w' for write). Defaults to "a".
        
    Methods:
        receive(): A method that runs as a daemon thread to continuously process and handle messages from the queue by passing them to the underlying FileHandler.
    
    Example:
        # Create an instance of MultiprocessingFileHandler
        log_handler = MultiprocessingFileHandler('path/to/logfile.log')
        
        # Set up a logger with this handler
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(log_handler)
        
        # Now, any log messages will be written to 'path/to/logfile.log' from multiple processes.
    """
    def __init__(self, path: Path, mode: str = "a"):
        logging.Handler.__init__(self)
        self._handler = logging.FileHandler(str(path), mode=mode)
        self.queue: 'mp.Queue[str]' = mp.Queue(-1)

        thrd = threading.Thread(target=self.receive)
        thrd.daemon = True
        thrd.start()

    def receive(self):
        while True:
            try:
                record = self.queue.get_nowait()
            except Exception:
                break
            else:
                self._handler.emit(record)

    def close(self):
        self._handler.close()
        logging.Handler.close(self)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.06s =============================
"""