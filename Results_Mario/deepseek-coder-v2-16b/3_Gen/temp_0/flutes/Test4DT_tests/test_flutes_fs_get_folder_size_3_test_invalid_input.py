
import pytest
from flutes.fs import get_folder_size  # Assuming the module is correctly imported
from unittest.mock import patch, Mock

def test_invalid_input():
    with pytest.raises(FileNotFoundError):
        with patch('flutes.fs.subprocess') as mock_subprocess:
            mock_subprocess.check_output.side_effect = FileNotFoundError("No such file or directory")
            get_folder_size('/nonexistent/path')
