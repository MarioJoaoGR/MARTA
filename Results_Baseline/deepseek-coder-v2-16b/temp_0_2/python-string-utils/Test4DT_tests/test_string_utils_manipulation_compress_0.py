
import pytest
from zlib import compress as zlib_compress
from base64 import b64encode
from string_utils.manipulation import compress

def test_compress_basic():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert len(compressed) < len(original), "Compressed string should be shorter than the original"

def test_compress_empty_string():
    with pytest.raises(ValueError):
        compress("")

@pytest.mark.xfail  # Expected to fail due to poor compression
def test_compress_unchanged():
    original = "This is a simple test string."
    compressed = compress(original)
    assert compressed == original, f"Compressed string should be the same as the original if it doesn't compress well: {compressed} != {original}"

def test_compress_specific_string():
    original = 'A' * 100 + 'B' * 50
    compressed = compress(original)