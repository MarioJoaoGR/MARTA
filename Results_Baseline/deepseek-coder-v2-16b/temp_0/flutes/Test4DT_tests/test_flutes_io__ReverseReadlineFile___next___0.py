
import pytest
from io import StringIO
from flutes.io import _ReverseReadlineFile

def test_reverse_readline_file_with_stringio():
    def reverse_lines_generator():
        yield "!dlrow ,olleH"  # This is the reversed line for demonstration purposes
    
    fp = StringIO("Hello, world!\n")
    gen = reverse_lines_generator()
    rev_readline = _ReverseReadlineFile(fp, gen)
    
    assert rev_readline.readline().strip() == "!dlrow ,olleH"

def test_reverse_readline_file_with_existing_file():
    import io
    
    with open('example.txt', 'w') as file:
        file.write("Hello, world!\nAnother line.\nYet another line.")
    
    with open('example.txt', 'rb') as file:
        gen = iter(lambda: next(file).decode().splitlines()[0], None)
        rev_readline = _ReverseReadlineFile(file, gen)
        
        assert next(rev_readline).strip() == "Hello, world!"