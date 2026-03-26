
import pytest
from pathlib import Path
from isort.place import _is_namespace_package

# Test cases for _is_namespace_package function

@pytest.mark.parametrize("path, src_extensions", [
    (Path("mypackage"), frozenset({"py"})),
    (Path("anotherpackage"), frozenset({"py"}))
])
def test_non_existent_directory(path, src_extensions):
    """Test if a non-existent directory returns False."""
    assert _is_namespace_package(path, src_extensions) is False

@pytest.mark.parametrize("path, src_extensions", [
    (Path("mypackage"), frozenset({"py"})),
    (Path("anotherpackage"), frozenset({"py"}))
])
def test_non_directory(path, src_extensions):
    """Test if a file returns False."""
    path.touch()