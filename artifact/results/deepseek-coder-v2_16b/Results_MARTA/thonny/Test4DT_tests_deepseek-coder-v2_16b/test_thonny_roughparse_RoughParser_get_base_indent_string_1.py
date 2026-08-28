
import pytest
from thonny.roughparse import RoughParser



def test_invalid_input():
    parser = RoughParser(indent_width=4, tabwidth=4)
    with pytest.raises(AssertionError):
        parser.set_str('invalid input')  # Assuming set_str raises AssertionError for invalid inputs