
import pytest
from flutes.io import progress_open

def test_edge_case_none():
    with pytest.raises(FileNotFoundError):
        progress_open(None)
