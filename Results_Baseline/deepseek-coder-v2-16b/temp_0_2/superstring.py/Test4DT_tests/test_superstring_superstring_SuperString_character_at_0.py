
import pytest
from superstring.superstring import SuperString

# Test initialization with valid content
def test_init_valid_content():
    s = SuperString("hello world")
    assert s._content == "hello world"

# Test character_at method with a valid index
def test_character_at_valid_index():
    s = SuperString("hello world")
    assert s.character_at(0) == 'h'
    assert s.character_at(4) == 'o'

# Test character_at method with an invalid index (out of range)
def test_character_at_invalid_index():
    s = SuperString("hello world")