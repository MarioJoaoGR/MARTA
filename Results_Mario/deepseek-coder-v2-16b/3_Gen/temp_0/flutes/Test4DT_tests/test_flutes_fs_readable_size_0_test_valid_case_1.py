
import pytest
from flutes.fs import readable_size

def test_valid_case_1():
    size = 1024 * 1024
    expected_output = "1.00M"
    assert readable_size(size) == expected_output
