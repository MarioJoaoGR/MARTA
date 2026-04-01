
import pytest
from superstring.superstring import SuperString

def test_valid_input():
    superstring = SuperString('Hello, World!')
    assert superstring.character_at(7) == 'W'
