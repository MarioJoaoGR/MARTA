
import pytest
from pathlib import Path
import logging
import multiprocessing as mp
import threading
from unittest.mock import patch, MagicMock
from flutes.log import MultiprocessingFileHandler

@pytest.fixture(scope="module")
def logger():
    log_path = "logs/app.log"
    handler = MultiprocessingFileHandler(Path(log_path))
    
    # Set up the logger with the handler
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    return logger

@pytest.fixture(scope="module")
def mock_log_path():
    # Mock the Path object to avoid actual file system access
    with patch('flutes.log.Path', spec=True) as mock_path:
        instance = mock_path.return_value
        instance.__truediv__.side_effect = lambda p, *args: f"{p}/{'/'.join(args)}"
        
        # Mock the log file path to avoid FileNotFoundError
        with patch('flutes.log.open', create=True) as mock_file:
            mock_file.return_value.__enter__.side_effect = lambda *args, **kwargs: open(*args, **kwargs)
            
            yield instance

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.06s =============================

"""