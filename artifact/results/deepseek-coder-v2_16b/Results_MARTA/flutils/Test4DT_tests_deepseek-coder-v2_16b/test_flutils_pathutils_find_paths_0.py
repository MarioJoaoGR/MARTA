
import pytest
from flutils.pathutils import find_paths
from pathlib import Path
import os

# Test scenario 1: Valid input
def test_valid_input():
    paths = list(find_paths('~/tmp/*'))
    assert isinstance(paths, list), "Expected a list of paths"
    for path in paths:
        assert isinstance(path, Path), f"Expected all paths to be instances of Path, but got {type(path)}"
        assert path.exists(), f"Path {path} does not exist"

# Test scenario 2: None input
def test_none_input():
    with pytest.raises(TypeError):
        list(find_paths(None))

# Test scenario 3: Invalid glob pattern
def test_invalid_pattern():
    paths = list(find_paths('this/is/an/invalid/*'))
    assert isinstance(paths, list), "Expected a list of paths"
    for path in paths:
        assert not path.exists(), f"Path {path} should not exist"
