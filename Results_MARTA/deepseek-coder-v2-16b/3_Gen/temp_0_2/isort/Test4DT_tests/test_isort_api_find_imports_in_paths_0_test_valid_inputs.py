
from pathlib import Path
from isort.api import find_imports_in_paths, Config, DEFAULT_CONFIG, ImportKey
from isort.identify import Import
from itertools import chain
import pytest

@pytest.fixture
def mock_valid_inputs():
    return [Path("dir1"), Path("dir2"), "file3.py"]

def test_find_imports_in_paths(mock_valid_inputs):
    imports = list(find_imports_in_paths(mock_valid_inputs))
    assert isinstance(imports, list), "Expected a list of Import objects"
    for imp in imports:
        assert isinstance(imp, Import), f"Expected {Import}, got {type(imp)}"
