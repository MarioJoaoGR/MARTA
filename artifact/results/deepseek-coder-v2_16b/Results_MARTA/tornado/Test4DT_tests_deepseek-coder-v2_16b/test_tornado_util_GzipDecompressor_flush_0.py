
import pytest
from tornado.util import GzipDecompressor
import zlib


def test_flush_method():
    decompressor = GzipDecompressor()
    compressed_data = b'x\x9c\xcbH\xcbM\x00\x04,\x02!'
    with pytest.raises(zlib.error):
        decompressor.decompress(compressed_data)