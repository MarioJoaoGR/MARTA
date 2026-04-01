
import pytest
from pathlib import Path
import subprocess
from unittest.mock import patch
from flutes.fs import get_folder_size

@pytest.mark.parametrize("path, expected", [
    (Path("/valid/directory"), 123456),  # Example values for the test
])
def test_get_folder_size(path, expected):
    with patch('subprocess.check_output') as mock_check_output:
        mock_check_output.return_value = b'123456\t/valid/directory\n'
        assert get_folder_size(path) == expected
