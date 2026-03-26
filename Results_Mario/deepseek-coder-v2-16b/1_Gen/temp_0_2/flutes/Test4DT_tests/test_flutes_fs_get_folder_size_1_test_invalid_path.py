
import pytest
from flutes.fs import get_folder_size
from pathlib import Path
import subprocess
from unittest.mock import patch

def test_invalid_path():
    with pytest.raises(FileNotFoundError):
        # Mock the subprocess call to raise a FileNotFoundError for an invalid path
        with patch('subprocess.check_output', side_effect=FileNotFoundError("No such file or directory")):
            get_folder_size(Path('/invalid/path'))
