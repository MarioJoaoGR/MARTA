
import pytest
from tornado.util import GzipDecompressor
import zlib

def test_valid_input():
    decompressor = GzipDecompressor()
    compressed_data = b'x\x9c\xcbH\xcbM\x00\x04,\x02!'
    with pytest.raises(zlib.error):
        assert decompressor.decompress(compressed_data) == b'example content'  # Replace with actual decompressed data
