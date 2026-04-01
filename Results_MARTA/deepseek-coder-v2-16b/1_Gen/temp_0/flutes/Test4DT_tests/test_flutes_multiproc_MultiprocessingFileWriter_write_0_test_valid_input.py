
import pytest
from pathlib import Path
from flutes.multiproc import MultiprocessingFileWriter  # Corrected import statement

def test_valid_input():
    writer = MultiprocessingFileWriter(Path('output.log'))
    assert isinstance(writer, MultiprocessingFileWriter)
