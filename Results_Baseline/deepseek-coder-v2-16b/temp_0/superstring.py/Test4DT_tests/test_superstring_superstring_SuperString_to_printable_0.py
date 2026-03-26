
import pytest
from superstring import SuperString

# Test cases for the to_printable method of the SuperString class
def test_to_printable_default():
    s = SuperString("Hello, world!")
    assert s.to_printable() == "Hello, world!"

def test_to_printable_with_start_and_end():
    s = SuperString("Hello, world!")
    assert s.to_printable(7, 12) == "world"

def test_to_printable_only_start():
    s = SuperString("Hello, world!")
    assert s.to_printable(7) == "world!"

def test_to_printable_only_end():
    s = SuperString("Hello, world!")