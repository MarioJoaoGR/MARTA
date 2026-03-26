
from io import StringIO
from contextlib import contextmanager
import pytest

@pytest.fixture(scope="module")
def in_memory_output_stream():
    yield StringIO(newline=None)

def test_in_memory_output_stream_context(in_memory_output_stream):
    assert isinstance(in_memory_output_stream, StringIO)
    assert in_memory_output_stream.newlines is None
