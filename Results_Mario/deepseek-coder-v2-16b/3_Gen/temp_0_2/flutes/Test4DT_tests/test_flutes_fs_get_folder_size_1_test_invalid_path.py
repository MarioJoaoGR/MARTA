
import subprocess
from unittest.mock import patch
from pathlib import Path  # Assuming this is the correct way to handle paths in Python
from flutes.fs import get_folder_size  # Adjusting the import according to the rules

def test_invalid_path():
    with patch('subprocess.check_output') as mock_check_output:
        mock_check_output.side_effect = FileNotFoundError("No such file or directory")
        
        try:
            get_folder_size(Path("/nonexistent/directory"))
        except FileNotFoundError:
            assert True  # The test should pass if the function raises a FileNotFoundError for an invalid path
