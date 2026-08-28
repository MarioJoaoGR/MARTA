
import pytest
import zlib
from tornado.util import GzipDecompressor

def test_decompress_valid_gzip_data():
    compressed_data = b'x\x9c\xcbH\xcb@\xa8\n\x00\x04,V\x02\x00\x1d\x01)\x0b'
    decompressor = GzipDecompressor()
    with pytest.raises(zlib.error):
        decompressed_data = decompressor.decompress(compressed_data)

def test_unconsumed_tail():
    compressed_data = b'x\x9c\xcbH\xcb@\xa8\n\x00\x04,V\x02\x00\x1d\x01)\x0b'
    decompressor = GzipDecompressor()
    with pytest.raises(zlib.error):
        while len(compressed_data) > 0:
            chunk = compressed_data[:10]
            if not chunk:
                break
            decompressed_chunk = decompressor.decompress(chunk)
