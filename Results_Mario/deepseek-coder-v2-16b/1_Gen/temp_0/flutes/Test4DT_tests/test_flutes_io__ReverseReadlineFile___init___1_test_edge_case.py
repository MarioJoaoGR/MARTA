
import pytest
from io import StringIO
from flutes.io import _ReverseReadlineFile

def reverse_lines_generator():
    yield "!dlrow ,olleH"  # This is the reversed line for demonstration purposes

@pytest.fixture
def setup_reverse_readline():
    fp = StringIO("Hello, world!\n")
    gen = reverse_lines_generator()
    return _ReverseReadlineFile(fp, gen)

def test_edge_case(setup_reverse_readline):
    rev_readline = setup_reverse_readline
    assert rev_readline.readline() == "!dlrow ,olleH"
