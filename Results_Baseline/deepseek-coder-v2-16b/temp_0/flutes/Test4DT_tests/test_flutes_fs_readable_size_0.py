
# Module: flutes.fs
# Import the function from its module
from flutes.fs import readable_size

def test_readable_size_bytes():
    assert readable_size(1024 * 1024) == "1.00M"
    assert readable_size(500000) == "488.28K"