
import pytest
from io import StringIO
import sys
from pysnooper.tracer import FileWriter

def test_valid_input_default_mode():
    # Setup
    output = StringIO()
    sys.stdout = output
    
    writer = FileWriter('example.txt', False)
    
    assert hasattr(writer, 'path')
    assert hasattr(writer, 'overwrite')
    assert writer.path == 'example.txt'
    assert not writer.overwrite

def test_valid_input_overwrite_true():
    # Setup
    output = StringIO()
    sys.stdout = output
    
    writer = FileWriter('overwrite_example.txt', True)
    
    assert hasattr(writer, 'path')
    assert hasattr(writer, 'overwrite')
    assert writer.path == 'overwrite_example.txt'
    assert writer.overwrite
