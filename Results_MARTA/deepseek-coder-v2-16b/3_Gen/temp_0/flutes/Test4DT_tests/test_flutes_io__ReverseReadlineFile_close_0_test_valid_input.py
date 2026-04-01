
import pytest
from flutes.io import _ReverseReadlineFile
from io import StringIO

def reverse_lines_generator():
    yield "!dlrow ,olleH"  # This is the reversed line for demonstration purposes

@pytest.fixture
def valid_input():
    fp = StringIO("Hello, world!\n")
    gen = reverse_lines_generator()
    return _ReverseReadlineFile(fp, gen)

def test_valid_input(valid_input):
    assert valid_input.readline() == "!dlrow ,olleH"
