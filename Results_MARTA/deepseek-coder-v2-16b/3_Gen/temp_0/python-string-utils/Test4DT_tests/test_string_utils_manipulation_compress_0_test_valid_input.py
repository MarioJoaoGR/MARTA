
import pytest
from string_utils.manipulation import compress, decompress

@pytest.mark.parametrize("input_string", ["hello world", "this is a test string"])
def test_valid_input(input_string):
    compressed = compress(input_string)
    assert isinstance(compressed, str), "Compressed output should be a string"
    decompressed = decompress(compressed)
    assert decompressed == input_string, f"Decompression failed for input: {input_string}"
