
import pytest
from pathlib import Path
from unittest.mock import patch

# Import the function to be tested
from isort.place import _is_module

@patch('os.path.exists', return_value=True)
def test_is_module_with_py_file(_mock_exists):
    path = Path("mypackage/module.py")
    assert _is_module(path) is True

@patch('os.path.exists', return_value=True)
def test_is_module_with_init_file(_mock_exists):
    path = Path("mypackage/__init__.py")
    assert _is_module(path) is True

@patch('os.path.exists', return_value=False)
def test_is_module_non_existent_path(_mock_exists):
    path = Path("nonexistentpath/file.txt")
    assert _is_module(path) is False

@patch('os.path.exists', side_effect=[True, True])
def test_is_module_with_multiple_extensions(_mock_exists):
    path = Path("mypackage/module.ext1")
    assert _is_module(path) is True

if __name__ == "__main__":
    pytest.main()
