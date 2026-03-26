
import subprocess
from pathlib import Path
import pytest
from unittest.mock import patch, Mock
from flutes.fs import get_folder_size  # Assuming the function is in this module

def test_invalid_path():
    with pytest.raises(FileNotFoundError):
        invalid_path = Path("nonexistent_directory")
        with patch('subprocess.check_output', side_effect=FileNotFoundError("No such file or directory")):
            get_folder_size(invalid_path)
