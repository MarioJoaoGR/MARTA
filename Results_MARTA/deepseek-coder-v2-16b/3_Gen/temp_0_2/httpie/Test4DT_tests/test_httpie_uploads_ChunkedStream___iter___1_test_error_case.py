
import pytest
from unittest.mock import patch, MagicMock
from httpie.uploads import ChunkedStream

def test_chunkedstream_iter():
    with patch('httpie.uploads.ChunkedStream.__iter__', return_value=iter([b'test1', b'test2'])):
        chunked_stream = ChunkedStream()
        iterator = iter(chunked_stream)
        assert next(iterator) == b'test1'
        assert next(iterator) == b'test2'
