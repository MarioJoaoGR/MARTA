
import pytest
from io import StringIO
from flutes.io import _ReverseReadlineFile

def test_valid_input():
    def custom_generator():
        yield 'First line\n'
        yield 'Second line\n'
        yield 'Third line\n'
    
    fp = StringIO('First line\nSecond line\nThird line\n')
    reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
    assert reverse_readline.readline() == 'First line\n'
    assert reverse_readline.readline() == 'Second line\n'
    assert reverse_readline.readline() == 'Third line\n'
