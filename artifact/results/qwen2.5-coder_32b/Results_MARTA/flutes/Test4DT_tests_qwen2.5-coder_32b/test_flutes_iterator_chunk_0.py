
import pytest
from flutes.iterator import chunk

def test_chunk_basic():
    # Test splitting a range of numbers into chunks of size 3
    result = list(chunk(3, range(10)))
    expected = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert result == expected

# Additional tests can be added here following the same structure if needed.
