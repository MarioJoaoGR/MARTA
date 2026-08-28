
import pytest
from string_utils.manipulation import compress

def test_valid_input():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert len(compressed) < len(original), "Compressed string should be shorter than the original"

def test_edge_case_empty_string():
    with pytest.raises(ValueError):
        compress('')

def test_invalid_compression_level():
    with pytest.raises(ValueError):
        compress('example', compression_level=-1)
