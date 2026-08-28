
import pytest
import zlib
from tornado.util import GzipDecompressor

@pytest.fixture(scope="module")
def decompressor():
    return GzipDecompressor()


def test_invalid_input(decompressor):
    with pytest.raises(zlib.error):
        invalid_data = b'invalid data'
        decompressor.decompress(invalid_data)