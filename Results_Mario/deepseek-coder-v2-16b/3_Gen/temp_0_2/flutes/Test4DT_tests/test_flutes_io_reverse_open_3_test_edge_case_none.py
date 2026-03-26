
import pytest
from pathlib import Path
from flutes.io import reverse_open

def test_edge_case_none():
    with pytest.raises(TypeError):
        reverse_open(None)
