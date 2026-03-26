
# Import the readable_size function from the flutes.fs module
from flutes.fs import readable_size

def test_valid_case_3():
    # Test case for valid input size
    assert readable_size(1024 * 1024) == "1.00M"
