
import pytest
from unittest.mock import patch, MagicMock
from isort.hooks import get_lines  # Correctly importing get_lines from isort.hooks

@pytest.mark.parametrize("command, expected", [
    (['ls', '-l'], ['total 12', '-rw-r--r--  1 user group  1024 Jan  1 12:34 file.txt', '...more lines...'])
])
def test_valid_input(command, expected):
    # Mocking the get_output function to return a predefined output for testing
    mock_stdout = MagicMock()
    mock_stdout.splitlines.return_value = expected
    
    with patch('isort.hooks.get_output', return_value=mock_stdout):
        result = get_lines(command)
        assert result == expected
