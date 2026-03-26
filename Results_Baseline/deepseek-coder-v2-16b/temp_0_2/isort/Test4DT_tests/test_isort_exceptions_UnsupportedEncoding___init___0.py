
from pathlib import Path

import pytest

from isort.exceptions import UnsupportedEncoding

# Test cases for the UnsupportedEncoding class

def test_basic_usage():
    try:
        raise UnsupportedEncoding("example_file.txt")
    except UnsupportedEncoding as e:
        assert str(e) == "Unknown or unsupported encoding in example_file.txt"