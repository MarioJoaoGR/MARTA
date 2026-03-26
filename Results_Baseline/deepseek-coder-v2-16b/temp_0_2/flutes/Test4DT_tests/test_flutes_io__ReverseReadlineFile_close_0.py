
import pytest
from io import IOBase
import io

# Import the function from the module
from flutes.io import _ReverseReadlineFile

def test_reverse_readline_file_init():
    # Create a file-like object with some text
    file_obj = io.StringIO("Line1\nLine2\nLine3\n")
    
    # Define a generator function that yields lines in reverse order
    def reverse_gen(fp):
        while True:
            line = fp.readline()
            if not line:
                break
            yield line
    
    # Instantiate the class with the file-like object and the custom generator
    rev_reader = _ReverseReadlineFile(fp=file_obj, gen=reverse_gen(file_obj))
    
    assert isinstance(rev_reader.fp, IOBase)