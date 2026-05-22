
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

def test_invalid_input():
    with patch('httpie.cli.argparser.HTTPieArgumentParser._body_from_file', side_effect=Exception("Invalid file input")):
        parser = HTTPieArgumentParser()
        mock_fd = MagicMock()
        
        with pytest.raises(Exception, match="Invalid file input"):
            parser._body_from_file(mock_fd)
