
import pytest
from pathlib import Path
import logging
import multiprocessing as mp
import threading
from flutes.log import MultiprocessingFileHandler

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test case for invalid path type
        MultiprocessingFileHandler(12345)  # Passing an integer instead of PathType
