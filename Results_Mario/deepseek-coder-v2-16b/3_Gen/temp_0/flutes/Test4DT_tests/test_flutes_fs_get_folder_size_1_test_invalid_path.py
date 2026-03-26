
import pytest
from pathlib import Path
from flutes.fs import get_folder_size  # Assuming the function is in this module
from unittest.mock import patch, Mock

def test_invalid_path():
    with patch('subprocess.check_output', side_effect=FileNotFoundError("No such file or directory")):
        invalid_path = Path("nonexistent_directory")
        with pytest.raises(FileNotFoundError):
            get_folder_size(invalid_path)
