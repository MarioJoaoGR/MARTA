
import pytest
from flutes.fs import readable_size

def test_valid_case_2():
    size = 500000
    expected_output = "488.28K"
    assert readable_size(size) == expected_output
