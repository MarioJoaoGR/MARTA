
# Module: pysnooper.tracer
import pytest
from pysnooper.tracer import FileWriter

# Test initialization with overwriting and appending modes
def test_file_writer_initialization():
    writer = FileWriter('example.txt', True)
    assert writer.path == 'example.txt'
    assert writer.overwrite is True
    
    append_writer = FileWriter('example.txt', False)
    assert writer.path == 'example.txt'  # Ensure the same path is used for both instances