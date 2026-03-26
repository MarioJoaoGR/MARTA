
# Import the necessary functions from the flutes.fs module
from flutes.fs import readable_size

def test_valid_input():
    # Test cases for valid input sizes
    assert readable_size(1024 * 1024) == "1.00M"
    assert readable_size(500000) == "488.28K"
    assert readable_size(123456789) == "117.74M"
    assert readable_size(1024) == "1.00K"
    assert readable_size(1024 * 1.5) == "1.50K"
    assert readable_size(1024 * 1024 * 2.75) == "2.75M"
    assert readable_size(1024 ** 3 * 1.98) == "1.98G"
    assert readable_size(1024 ** 4 * 1.12) == "1.12T"
    assert readable_size(1024 ** 5 * 1.01) == "1.01P"
