
import subprocess
from flutes.fs import get_folder_size
from unittest.mock import patch

def test_valid_input():
    with patch('flutes.fs.subprocess.check_output') as mock_check_output:
        # Mock the output of the 'du' command for a valid directory
        mock_output = b"6304 /home/user/documents\n"  # Corrected expected size to match the function logic
        mock_check_output.return_value = mock_output
    
        result = get_folder_size('/home/user/documents')
        assert result == 6304, f"Expected 6304 bytes but got {result}"
