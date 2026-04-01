
import subprocess
from unittest.mock import patch, MagicMock
import pytest

def get_lines(command: list[str]) -> list[str]:
    """Run a command and return lines of output

    :param str command: the command to run
    :returns: list of whitespace-stripped lines output by command
    """
    stdout = subprocess.run(command, capture_output=True, text=True).stdout
    return [line.strip() for line in stdout.splitlines()]

@pytest.fixture
def mock_subprocess():
    with patch('subprocess.run') as mock_run:
        yield mock_run

def test_valid_case(mock_subprocess):
    # Mock the subprocess.run to return a sample output
    mock_stdout = "line1\nline2\nline3"
    mock_return_value = MagicMock()
    mock_return_value.stdout = mock_stdout
    mock_subprocess.return_value = mock_return_value

    # Call the function with a sample command
    result = get_lines(['ls', '-l'])

    # Assert that the output is as expected
    assert result == ['line1', 'line2', 'line3']
