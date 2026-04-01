
import pytest
from io import StringIO
from flutes.io import _ReverseReadlineFile

def reverse_lines_generator():
    yield "!dlrow ,olleH"  # This is the reversed line for demonstration purposes

def test_valid_case():
    fp = StringIO("Hello, world!\n")
    gen = reverse_lines_generator()
    rev_readline = _ReverseReadlineFile(fp, gen)
    
    assert rev_readline.readline() == "!dlrow ,olleH"
