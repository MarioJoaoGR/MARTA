
import pytest
from string_utils.manipulation import compress

def test_compress_basic():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert isinstance(compressed, str)
    assert len(compressed) < len(original)
