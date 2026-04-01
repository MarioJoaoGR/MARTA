
import pytest
from io import StringIO, TextIOBase
from contextlib import contextmanager

@contextmanager
def capture_output():
    out = StringIO()
    yield out

def test_in_memory_output_stream_context():
    from isort.api import _in_memory_output_stream_context
    
    with _in_memory_output_stream_context() as stream:
        assert isinstance(stream, StringIO)
        assert stream.newlines is None  # Check that newline handling is set to None
        
        # Example of writing to the in-memory stream
        print("Hello, World!", file=stream)
        assert stream.getvalue() == "Hello, World!\n"
