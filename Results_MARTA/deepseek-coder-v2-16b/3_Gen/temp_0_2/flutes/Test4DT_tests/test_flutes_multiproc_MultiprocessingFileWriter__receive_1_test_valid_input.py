
import pytest
from flutes.multiproc import MultiprocessingFileWriter  # Assuming the correct module path

def test_valid_input():
    writer = MultiprocessingFileWriter('testfile.log')
    assert isinstance(writer, MultiprocessingFileWriter)
