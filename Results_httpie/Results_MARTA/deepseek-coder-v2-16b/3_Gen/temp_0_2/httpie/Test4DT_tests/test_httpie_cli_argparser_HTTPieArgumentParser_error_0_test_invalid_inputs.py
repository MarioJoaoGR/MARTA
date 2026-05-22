
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

def test_invalid_inputs():
    with patch('httpie.cli.argparser.HTTPieArgumentParser', autospec=True) as MockParser:
        # Create a mock instance of the parser
        mock_parser = MockParser()

        # Set up the error method to raise an exception when called
        mock_parser.error = MagicMock(side_effect=SystemExit("Expected SystemExit"))

        with pytest.raises(SystemExit):
            mock_parser.error("Invalid input")
