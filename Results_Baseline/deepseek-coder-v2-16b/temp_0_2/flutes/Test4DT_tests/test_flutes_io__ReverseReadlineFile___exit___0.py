
import io
import pytest
from flutes.io import _ReverseReadlineFile

# Test initialization with a file-like object and a generator function
def test_init():
    def custom_generator():
        yield b'H'
        yield b'e'
        yield b'l'
        yield b'l'
        yield b'o'
    
    fp = io.BytesIO(b'Hello, World!')
    reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
    assert reverse_readline.fp == fp
    assert list(reverse_readline.gen) == [b'H', b'e', b'l', b'l', b'o']

# Test reading lines from the generator function
def test_readline():
    def custom_generator():
        yield b'H'
        yield b'e'
        yield b'l'
        yield b'l'
        yield b'o'
    
    fp = io.BytesIO(b'Hello, World!')
    reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
    assert reverse_readline.readline().decode() == 'H'
    assert reverse_readline.readline().decode() == 'e'
    assert reverse_readline.readline().decode() == 'l'
    assert reverse_readline.readline().decode() == 'l'
    assert reverse_readline.readline().decode() == 'o'

# Test closing the file pointer
def test_close():
    def custom_generator():
        yield b'H'
        yield b'e'
        yield b'l'
        yield b'l'
        yield b'o'
    
    fp = io.BytesIO(b'Hello, World!')
    reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
    assert not fp.closed
    reverse_readline.close()
    assert fp.closed

# Test raising an exception during reading and ensure the file pointer is closed properly
def test_exception_handling():
    class CustomException(Exception): pass
    
    def custom_generator():
        yield b'H'
        raise CustomException("Generator error")
    
    fp = io.BytesIO(b'Hello, World!')
    reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
    with pytest.raises(CustomException):
        while True:
            reverse_readline.readline()
    