
# Import the booleanize function from the string_utils module
from string_utils import booleanize

def test_booleanize_empty_string():
    assert booleanize('') is False
