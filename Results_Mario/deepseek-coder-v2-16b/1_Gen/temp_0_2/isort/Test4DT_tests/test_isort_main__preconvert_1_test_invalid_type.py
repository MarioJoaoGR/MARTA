
import pytest
from pathlib import Path
from isort.main import _preconvert

def test_invalid_type():
    with pytest.raises(TypeError):
        _preconvert("not a valid type")
