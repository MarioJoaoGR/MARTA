
import pytest
from flutes.multiproc import MultiprocessingFileWriter  # Corrected import statement

def test_valid_input():
    writer = MultiprocessingFileWriter('testfile.log')
    assert isinstance(writer, MultiprocessingFileWriter)
