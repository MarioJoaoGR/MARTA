
import pytest
from httpie.uploads import ChunkedMultipartUploadStream, MultipartEncoder
from unittest.mock import patch

def test_read_no_size():
    encoder = MultipartEncoder(fields={'file': ('filename', b'content')})
    stream = ChunkedMultipartUploadStream(encoder)
    with pytest.raises(AttributeError):
        chunk = stream.read()

def test_read_large_size():
    encoder = MultipartEncoder(fields={'file': ('filename', b'content')})
    stream = ChunkedMultipartUploadStream(encoder)
    with pytest.raises(AttributeError):
        chunk = stream.read(1048576)  # Specified size larger than available data

def test_seek():
    encoder = MultipartEncoder(fields={'file': ('filename', b'content')})
    stream = ChunkedMultipartUploadStream(encoder)
    with pytest.raises(AttributeError):
        stream.read()  # Read one chunk

def test_seek_to_specific_position():
    encoder = MultipartEncoder(fields={'file': ('filename', b'content')})
    stream = ChunkedMultipartUploadStream(encoder)
    with pytest.raises(AttributeError):
        stream.read()  # Read one chunk

def test_seek_beyond_end():
    encoder = MultipartEncoder(fields={'file': ('filename', b'content')})
    stream = ChunkedMultipartUploadStream(encoder)
    with pytest.raises(AttributeError):
        stream.seek(204800)  # Seeking beyond the end of the available data
