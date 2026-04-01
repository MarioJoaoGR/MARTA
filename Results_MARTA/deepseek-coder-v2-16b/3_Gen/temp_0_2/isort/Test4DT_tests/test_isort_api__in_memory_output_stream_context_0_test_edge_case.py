
from io import StringIO
from contextlib import contextmanager
import pytest

@contextmanager
def _in_memory_output_stream_context():
    stream = StringIO(newline=None)
    yield stream

def test_edge_case():
    with _in_memory_output_stream_context() as output_stream:
        # Perform operations on the output_stream, such as writing sorted import statements
        print("Hello, World!", file=output_stream)
        assert output_stream.getvalue().strip() == "Hello, World!"
