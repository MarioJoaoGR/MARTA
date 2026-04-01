
import logging
import multiprocessing as mp
import threading
import traceback
import sys
from pathlib import Path

class MultiprocessingFileHandler(logging.Handler):
    """
    Class for handling multiprocessing logging to a single file using a queue.
    
    This class allows multiple processes to log messages to the same file by utilizing a shared queue. It is based on the implementation from Matt Gathu's blog post titled "multiprocessing-logging-in-python".

    Parameters:
        path (PathType): The file path where logs will be written. This should be a string or any object that can be converted to a Path-like object.
        mode (str, optional): The mode in which the log file is opened. Defaults to "a" (append). Other possible values include "w" (write) and "x" (exclusive creation).

    Example:
        To use this class, you would typically create an instance of it with a specific log file path and mode. Here's how you might do that:
        
        ```python
        import multiprocessing_logging_handler as mplh
        from pathlib import Path

        # Define the log file path and mode
        log_path = Path("logs/application.log")
        log_mode = "a"

        # Create an instance of MultiprocessingFileHandler
        handler = mplh.MultiprocessingFileHandler(log_path, mode=log_mode)
        
        # Configure your logging setup to use this handler
        logger = logging.getLogger()
        logger.addHandler(handler)
        ```
    
    This will set up a logger that can be used across multiple processes to log messages to the same file without conflicts.
    """
    def __init__(self, path: PathType, mode: str = "a"):
        logging.Handler.__init__(self)
        self._handler = logging.FileHandler(path, mode=mode)
        self.queue: 'mp.Queue[str]' = mp.Queue(-1)

        thrd = threading.Thread(target=self.receive)
        thrd.daemon = True
        thrd.start()

    def receive(self):
        while True:
            try:
                record = self.queue.get()
                self._handler.emit(record)
            except (KeyboardInterrupt, SystemExit):
                raise
            except EOFError:
                break
            except:
                traceback.print_exc(file=sys.stderr)
```

And here's the test case for `test_receive`:

```python
import pytest
import logging
from flutes.log import MultiprocessingFileHandler
import multiprocessing as mp
import threading
import time
import os
import sys
import traceback

@pytest.fixture(scope="module")
def setup_logger():
    log_path = "test_logfile.log"
    handler = MultiprocessingFileHandler(log_path)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    yield handler, logger
    os.remove(log_path)  # Clean up the log file after the test

def test_receive(setup_logger):
    handler, logger = setup_logger
    
    # Log a message to the queue from a separate process
    def log_from_process():
        time.sleep(0.1)  # Wait for the logger to be set up
        logger.info("Test log message")
    
    p = mp.Process(target=log_from_process)
    p.start()
    p.join()
    
    # Check if the log file contains the expected message
    with open(handler._handler.baseFilename, 'r') as f:
        logs = f.readlines()
        assert "Test log message" in logs[-1]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_input
flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_input.py:62:9: E0001: Parsing failed: 'unterminated string literal (detected at line 62) (Test4DT_tests.test_flutes_log_MultiprocessingFileHandler_receive_0_test_valid_input, line 62)' (syntax-error)


"""