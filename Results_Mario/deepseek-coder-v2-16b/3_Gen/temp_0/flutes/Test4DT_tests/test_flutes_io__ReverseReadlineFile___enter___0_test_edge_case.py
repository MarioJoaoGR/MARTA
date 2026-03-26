
import pytest
from unittest.mock import MagicMock
from flutes.io import _ReverseReadlineFile

@pytest.fixture
def mock_gen():
    def gen():
        yield "!dlrow ,olleH"  # This is the reversed line for demonstration purposes
    return gen()

def test_edge_case(mock_gen):
    fp = MagicMock()
    rev_readline = _ReverseReadlineFile(fp, mock_gen)
    
    assert rev_readline.readline() == "!dlrow ,olleH"
