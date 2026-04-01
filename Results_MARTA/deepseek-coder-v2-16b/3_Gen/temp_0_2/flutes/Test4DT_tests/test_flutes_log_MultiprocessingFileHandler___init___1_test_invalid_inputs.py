
import pytest
from flutes.log import MultiprocessingFileHandler
import multiprocessing as mp
import threading
import logging
from pathlib import Path

def test_invalid_inputs():
    # Test case for invalid input types
    with pytest.raises(TypeError):
        MultiprocessingFileHandler(12345)  # Invalid type for path (int instead of str or Path)
    
    # Test case for invalid mode value
    with pytest.raises(ValueError):
        MultiprocessingFileHandler("path/to/logfile.log", mode="invalid_mode")  # Invalid mode value
