
import subprocess
from pathlib import Path
from unittest.mock import patch, MagicMock
import flutes.fs  # Assuming the module is named flutes.fs and contains get_folder_size function

def test_get_folder_size_valid_input():
    with patch('subprocess.check_output') as mock_check_output:
        # Mocking the output of the 'du' command
        mock_output = b"12345 /path/to/folder\n"
        mock_check_output.return_value = mock_output
        
        path = Path("/path/to/folder")
        result = flutes.fs.get_folder_size(path)
        
        # Assert the function call and the expected result
        assert result == 12345
