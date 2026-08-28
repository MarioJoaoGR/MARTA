
import pytest
from apimd.parser import code



def test_no_special_characters():
    """Test the case where the input does not contain special characters."""
    assert code("example_text") == '`example_text`'

def test_empty_string():
    """Test the case where the input is an empty string."""
    assert code("") == ' '

