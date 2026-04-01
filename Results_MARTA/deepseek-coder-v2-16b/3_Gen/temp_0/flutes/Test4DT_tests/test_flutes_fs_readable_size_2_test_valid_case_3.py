
import pytest
from flutes.fs import readable_size

def test_valid_case_3():
    size = 123456789
    expected_output = "117.74M"
    assert readable_size(size) == expected_output
