
import pytest
from pathlib import Path
from unittest.mock import MagicMock
from isort.place import _is_namespace_package

def test_invalid_input():
    mock_path = MagicMock()
    mock_path.__str__.return_value = 'mocked_dir'
    mock_path.exists.return_value = False
    
    assert not _is_namespace_package(mock_path, frozenset({"py", "pyi"}))
