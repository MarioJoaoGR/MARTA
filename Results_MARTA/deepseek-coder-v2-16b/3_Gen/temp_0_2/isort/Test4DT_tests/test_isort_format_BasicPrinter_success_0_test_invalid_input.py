
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
from isort.format import BasicPrinter

def test_invalid_input():
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        # Create an instance of BasicPrinter with invalid input
        printer = BasicPrinter(error='Invalid input error', success='Success message')
        
        # Call the method that should handle invalid input
        printer.success("invalid message")
        
        # Check if the output is as expected
        assert mock_stdout.getvalue().strip() == 'Success message'
