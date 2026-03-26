
import io
import pytest
from flutes.io import _ReverseReadlineFile

# Test initialization with a file-like object and a generator function
def test_init():
    def custom_generator():
        yield "Line3\n"
        yield "Line2\n"
        yield "Line1\n"
    
    fp = io.StringIO("Line1\nLine2\nLine3\n")
    reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
    assert reverse_readline.fp == fp
    assert list(reverse_readline.gen) == ["Line3\n", "Line2\n", "Line1\n"]

# Test reading lines from the file-like object in reverse order
def test_readline():
    def custom_generator():
        yield "Line3\n"
        yield "Line2\n"
        yield "Line1\n"
    
    fp = io.StringIO("Line1\nLine2\nLine3\n")
    reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
    assert reverse_readline.readline() == "Line3\n"
    assert reverse_readline.readline() == "Line2\n"
    assert reverse_readline.readline() == "Line1\n"
    with pytest.raises(StopIteration):
        reverse_readline.readline()  # End of file

# Test reading lines from the file-like object in reverse order with a different generator function
def test_different_generator():
    def custom_generator():
        yield b'H'
        yield b'e'
        yield b'l'
        yield b'l'
        yield b'o'
    
    fp = io.BytesIO(b'Hello, World!')
    reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
    assert reverse_readline.readline() == b'H'
    assert reverse_readline.readline() == b'e'
    assert reverse_readline.readline() == b'l'
    assert reverse_readline.readline() == b'l'
    assert reverse_readline.readline() == b'o'
    with pytest.raises(StopIteration):
        reverse_readline.readline()  # End of file

# Test initialization with a generator function and an empty file-like object
def test_init_with_empty_file():
    def custom_generator():
        yield "Line1\n"
    
    fp = io.StringIO("")
    reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
    assert reverse_readline.fp == fp
    assert list(reverse_readline.gen) == ["Line1\n"]

# Test reading lines from an empty file-like object
def test_readline_on_empty_file():
    def custom_generator():
        yield "Line1\n"
    
    fp = io.StringIO("")
    reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
    assert reverse_readline.readline() == "Line1\n"
    with pytest.raises(StopIteration):
        reverse_readline.readline()  # End of file
