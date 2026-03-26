
import pytest
from io import StringIO
from flutes.io import _ReverseReadlineFile

def test_readline():
    def reverse_lines_generator():
        yield b'!dlrow ,olleH'  # This is the reversed line for demonstration purposes
    
    fp = StringIO("Hello, world!\n")
    gen = reverse_lines_generator()
    rev_readline = _ReverseReadlineFile(fp, gen)
    
    assert rev_readline.readline() == b'!dlrow ,olleH'

def test_readline_empty():
    def reverse_lines_generator():
        yield from []  # This will cause StopIteration when trying to read a line
    
    fp = StringIO("Hello, world!\n")
    gen = reverse_lines_generator()
    rev_readline = _ReverseReadlineFile(fp, gen)
    