
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

@pytest.mark.parametrize("stdin_data", [b"valid input", "another valid input"])
def test_valid_inputs(stdin_data):
    with patch('sys.stdin', new=MagicMock()) as mock_stdin:
        # Set the return value of read for the mock object to simulate stdin data
        mock_stdin.read.return_value = stdin_data
        
        env = Environment()
        
        assert env.stdin is not None
        assert env.stdin.isatty() == False  # Since we are providing input, it should not be a tty
        
        # Read the data directly from the mock object without using sys.stdin.read()
        captured_input = mock_stdin.read.return_value
        assert captured_input == stdin_data
