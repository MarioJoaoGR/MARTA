
import pytest
from flutes.fs import get_file_lines  # Assuming the module is correctly imported
import subprocess
from unittest.mock import patch, Mock

def test_invalid_path():
    with pytest.raises(FileNotFoundError):
        invalid_path = "nonexistent_file.txt"
        with patch('subprocess.check_output', side_effect=FileNotFoundError("File not found")):
            get_file_lines(invalid_path)
