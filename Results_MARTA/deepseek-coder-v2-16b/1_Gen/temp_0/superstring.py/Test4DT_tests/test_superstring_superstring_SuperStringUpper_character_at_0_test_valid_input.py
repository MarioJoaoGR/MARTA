
import pytest
from superstring.superstring import SuperString, SuperStringUpper

def test_valid_input():
    superstring_upper = SuperStringUpper(SuperString("Hello, World!"))
    assert superstring_upper.character_at(7) == 'W'
