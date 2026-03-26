
# Module: isort.exceptions
from pathlib import Path

import pytest

from isort.exceptions import UnsupportedEncoding


# Test Case 1: Raising an Exception with a Specific Filename
def test_unsupported_encoding_with_specific_filename():
    with pytest.raises(UnsupportedEncoding) as exc_info:
        raise UnsupportedEncoding("example_file.txt")
    assert str(exc_info.value) == "Unknown or unsupported encoding in example_file.txt"