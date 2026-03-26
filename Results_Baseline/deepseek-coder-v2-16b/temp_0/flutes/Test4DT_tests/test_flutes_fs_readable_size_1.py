
# Module: flutes.fs
from flutes.fs import readable_size

def test_readable_size_bytes():
    assert readable_size(1024 * 1024) == "1.00M"
    assert readable_size(500000) == "488.28K"

# Additional tests for different sizes and edge cases
def test_readable_size_small():
    assert readable_size(1023) == "1023.00"
    assert readable_size(1024) == "1.00K"

def test_readable_size_large():
    assert readable_size(1024 * 1024 * 1024) == "1.00G"