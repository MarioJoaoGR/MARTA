
# Import the necessary function from the module
from flutes.fs import readable_size

def test_valid_case_2():
    # Test case for valid input size
    assert readable_size(500000, 2) == "488.28K"
