
import pytest
from io import StringIO
from flutes.io import _ReverseReadlineFile

def test_reverse_readline_file():
    # Create a mock file-like object with some data
    fp = StringIO("Hello, World!")
    
    # Define a generator that yields characters in reverse order
    def custom_generator():
        yield "H"
        yield "e"
        yield "l"
        yield "l"
        yield "o"
    
    # Instantiate the class and use it within a with statement
    rr = _ReverseReadlineFile(fp=fp, gen=custom_generator())
    assert rr.readline() == "H"
    assert rr.readline() == "e"
    assert rr.readline() == "l"
    assert rr.readline() == "l"
    assert rr.readline() == "o"

def test_reverse_readline_file_with_mock_file():
    # Create a mock file-like object with some data
    mock_file = StringIO("Hello, World!")
    
    # Define a generator that yields characters in reverse order
    def custom_generator():
        yield "H"
        yield "e"
        yield "l"
        yield "l"
        yield "o"
    
    # Instantiate the class and use it within a with statement
    rr = _ReverseReadlineFile(fp=mock_file, gen=custom_generator())
    assert rr.readline() == "H"
    assert rr.readline() == "e"
    assert rr.readline() == "l"
    assert rr.readline() == "l"
    assert rr.readline() == "o"

def test_reverse_readline_file_empty():
    # Create a mock file-like object with no data
    fp = StringIO("")
    
    # Define an empty generator
    def custom_generator():
        yield from []
    
    # Instantiate the class and use it within a with statement
    rr = _ReverseReadlineFile(fp=fp, gen=custom_generator())