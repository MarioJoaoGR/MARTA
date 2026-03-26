
import pytest
from pathlib import Path
import multiprocessing as mp
import threading
from flutes.multiproc import MultiprocessingFileWriter

@pytest.fixture
def setup_writer():
    return MultiprocessingFileWriter(Path("testfile.txt"))

def test_invalid_inputs(setup_writer):
    writer = setup_writer
    with pytest.raises(TypeError):
        # This should raise a TypeError because the function expects 3 arguments, but only 0 are provided
        writer.__exit__()
