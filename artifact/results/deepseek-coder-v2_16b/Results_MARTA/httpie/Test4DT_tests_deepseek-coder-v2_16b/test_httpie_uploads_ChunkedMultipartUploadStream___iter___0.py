
import pytest
from httpie.uploads import ChunkedMultipartUploadStream
from requests_toolbelt.multipart.encoder import MultipartEncoder

def test_read_method():
    encoder = MultipartEncoder(fields={'file': ('filename', b'content')})
    stream = ChunkedMultipartUploadStream(encoder)
    with pytest.raises(AttributeError):
        chunk = stream.read()

def test_seek_method():
    encoder = MultipartEncoder(fields={'file': ('filename', b'content')})
    stream = ChunkedMultipartUploadStream(encoder)
    with pytest.raises(AttributeError):
        initial_position = stream.tell()

def test_writable_method():
    encoder = MultipartEncoder(fields={'file': ('filename', b'content')})
    stream = ChunkedMultipartUploadStream(encoder)
    with pytest.raises(AttributeError):
        assert not stream.writable()
