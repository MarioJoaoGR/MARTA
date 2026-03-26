
import pytest
from flutes.io import _ReverseReadlineFile
from io import StringIO

def reverse_lines_generator():
    yield "!dlrow ,olleH"  # This is the reversed line for demonstration purposes

@pytest.fixture
def setup_reverse_readline():
    fp = StringIO("Hello, world!\n")
    gen = reverse_lines_generator()
    return _ReverseReadlineFile(fp, gen)

def test_readline(setup_reverse_readline):
    rev_readline = setup_reverse_readline
    assert rev_readline.readline() == "!dlrow ,olleH"

def test_close(setup_reverse_readline):
    rev_readline = setup_reverse_readline
    rev_readline.close()
    with pytest.raises(ValueError):
        rev_readline.fp.read()
