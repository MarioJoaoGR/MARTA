
import pytest
from flutes.io import _ReverseReadlineFile
from io import StringIO

def reverse_lines_generator():
    yield "!dlrow ,olleH"  # This is the reversed line for demonstration purposes

@pytest.fixture
def setup_reverse_readline():
    fp = StringIO("Hello, world!\n")
    gen = reverse_lines_generator()
    rev_readline = _ReverseReadlineFile(fp, gen)
    return rev_readline

def test_edge_case_none(setup_reverse_readline):
    rev_readline = setup_reverse_readline
    assert next(rev_readline).rstrip('\n') == "!dlrow ,olleH"
