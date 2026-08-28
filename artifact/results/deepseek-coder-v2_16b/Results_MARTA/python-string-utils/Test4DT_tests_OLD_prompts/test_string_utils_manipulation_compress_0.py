
import pytest
from zlib import compress as zlib_compress, decompress as zlib_decompress
import base64

def compress(input_string: str, encoding: str = 'utf-8', compression_level: int = 9) -> str:
    """
    Compresses the given input string using zlib and base64 libraries for efficient storage in memory-constrained environments or when a shorter representation is desired. The compressed string can be later restored to its original form using the `decompress()` function.

    **Bear in mind:**
    Besides the provided `compression_level`, the compression result (how much the string is actually compressed
    by resulting into a shorter string) depends on 2 factors:

    1. The amount of data (string size): short strings might not provide a significant compression result\
    or even be longer than the given input string (this is due to the fact that some bytes have to be embedded\
    into the compressed string in order to be able to restore it later on)\

    2. The content type: random sequences of chars are very unlikely to be successfully compressed, while the best\
    compression result is obtained when the string contains several recurring char sequences (like in the example).

    Behind the scenes this method makes use of the standard Python's zlib and base64 libraries.

    *Examples:*

    >>> original = ' '.join(['word n{}'.format(n) for n in range(20)])
    >>> compressed = compress(original)
    >>> print(len(compressed))  # The length of the compressed string will be shorter than the original.

    :param input_string: String to compress (must be not empty or a ValueError will be raised).
    :type input_string: str
    :param encoding: String encoding (default to "utf-8").
    :type encoding: str
    :param compression_level: A value between 0 (no compression) and 9 (best compression), default to 9.
    :type compression_level: int
    :return: Compressed string.
    """
    if input_string == "":
        raise ValueError("Input string is empty, cannot be compressed.")
    if not (0 <= compression_level <= 9):
        raise ValueError("Invalid compression level provided. Compression level must be between 0 and 9.")
    
    # Compress the string using zlib
    compressed = zlib_compress(input_string.encode(encoding), compression_level)
    # Encode the compressed data in base64 to make it a valid ASCII string
    return base64.b64encode(compressed).decode('utf-8')

def decompress(compressed_string: str, encoding: str = 'utf-8') -> str:
    """
    Decompresses the given compressed string back to its original form.

    :param compressed_string: The compressed string to be decompressed (must be not empty or a ValueError will be raised).
    :type compressed_string: str
    :param encoding: String encoding (default to "utf-8").
    :type encoding: str
    :return: Decompressed string.
    """
    if compressed_string == "":
        raise ValueError("Compressed string is empty, cannot be decompressed.")
    
    # Decode the base64 string back to bytes
    compressed = base64.b64decode(compressed_string)
    # Decompress the data using zlib
    return zlib_decompress(compressed).decode(encoding)

# Test cases
def test_valid_input():
    original = ' '.join(['word n{}'.format(n) for n in range(20)])
    compressed = compress(original)
    assert len(compressed) < len(original), "Compressed string should be shorter than the original"
    decompressed = decompress(compressed)
    assert decompressed == original, "Decompressed string does not match the original"

def test_edge_case_empty_string():
    with pytest.raises(ValueError):
        compress("")

def test_invalid_compression_level():
    with pytest.raises(ValueError):
        compress("example", compression_level=-1)
