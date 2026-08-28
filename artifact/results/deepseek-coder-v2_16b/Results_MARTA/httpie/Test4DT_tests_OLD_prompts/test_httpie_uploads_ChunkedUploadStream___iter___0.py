
import pytest
from unittest.mock import patch, MagicMock
from httpie.uploads import ChunkedUploadStream
from collections.abc import Iterable


def test_invalid_input():
    def process_chunk(chunk):
        assert not isinstance(chunk, Iterable)
        return chunk
    
    with pytest.raises(TypeError):  # Expecting a TypeError due to non-iterable stream
        upload_stream = ChunkedUploadStream(stream=None, callback=process_chunk)
        for _ in upload_stream:
            pass