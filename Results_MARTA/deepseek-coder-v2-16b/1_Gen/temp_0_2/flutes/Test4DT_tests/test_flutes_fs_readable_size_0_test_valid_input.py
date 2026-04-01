
import pytest
from flutes.fs import readable_size

def test_valid_input():
    assert readable_size(1024 * 1024) == "1.00M"
    assert readable_size(500000) == "488.28K"
    assert readable_size(123456789) == "117.74M"
    assert readable_size(1024) == "1.00K"
    assert readable_size(1024 * 1024 * 1024) == "1.00G"
