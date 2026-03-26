
import pytest
from string_utils.manipulation import compress, decompress

@pytest.mark.parametrize("input_string", [''.join(['word n{}'.format(n) for n in range(20)])])
def test_valid_input(input_string):
    compressed = compress(input_string)
    assert isinstance(compressed, str), "Compressed output should be a string"
    decompressed = decompress(compressed)
    assert decompressed == input_string, "Decompressed string should match the original input string"
