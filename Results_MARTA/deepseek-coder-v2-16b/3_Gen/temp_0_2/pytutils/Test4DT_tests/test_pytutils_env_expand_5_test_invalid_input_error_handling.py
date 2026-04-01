
import pytest
from unittest.mock import patch
import os
from pytutils.env import expand

@pytest.mark.parametrize("invalid_input", ["~invalid_user", "$INVALID_VAR/Projects", "~/nonexistent_directory"])
def test_invalid_input_error_handling(invalid_input):
    with patch('os.path.expandvars') as mock_expandvars:
        with patch('os.path.expanduser') as mock_expanduser:
            # Mock the behavior of expandvars and expanduser to return the input value
            mock_expandvars.return_value = invalid_input
            mock_expanduser.return_value = invalid_input
            
            result = expand(invalid_input)
            assert result == invalid_input, f"Expected {invalid_input}, but got {result}"
