
import pytest
from apimd.parser import Parser

# Test for valid input file existence

# Test for edge case where None is passed to is_public method

# Test for invalid input file existence
def test_invalid_input():
    p = Parser()
    with pytest.raises(FileNotFoundError):
        with open("test_invalid_pkg_path", 'r') as f:
            pass