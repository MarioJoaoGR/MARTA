
import pytest
from pysnooper.utils import WritableStream, _check_methods

def test_writable_stream_subclasshook():
    class MockWritableStream(WritableStream):
        pass
    
    assert issubclass(MockWritableStream, WritableStream)
    assert _check_methods(MockWritableStream, 'write') is True
