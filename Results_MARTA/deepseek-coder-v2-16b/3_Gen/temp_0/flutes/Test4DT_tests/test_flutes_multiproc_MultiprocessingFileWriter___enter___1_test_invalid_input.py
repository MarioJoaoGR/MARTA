
import pytest
from pathlib import Path
import multiprocessing as mp
import threading
from typing import IO, Any
from flutes.multiproc import MultiprocessingFileWriter

@pytest.fixture
def invalid_input():
    return None  # This is an invalid input type for the constructor of MultiprocessingFileWriter

def test_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        MultiprocessingFileWriter(invalid_input)
