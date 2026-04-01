
import pytest
from flutes.io import _ReverseReadlineFile
from io import StringIO

def test_valid_input():
    # Define a generator function that yields the reversed lines
    def reverse_lines_generator():
        yield "!dlrow ,olleH"  # This is the reversed line for demonstration purposes

    # Create a mock file-like object with sample data
    data = "Hello, world!\n"
    fp = StringIO(data)

    # Create an instance of _ReverseReadlineFile with the file-like object and generator function
    rev_readline = _ReverseReadlineFile(fp, reverse_lines_generator())

    # Iterate over the lines in reverse order and assert the result
    assert next(rev_readline) == "!dlrow ,olleH\n"
