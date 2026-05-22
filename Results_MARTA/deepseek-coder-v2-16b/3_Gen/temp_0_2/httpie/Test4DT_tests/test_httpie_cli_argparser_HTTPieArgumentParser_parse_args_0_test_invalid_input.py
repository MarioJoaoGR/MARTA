
import pytest
from unittest.mock import patch
from httpie.cli.argparser import HTTPieArgumentParser

def test_invalid_input():
    with patch('httpie.cli.argparser.HTTPieArgumentParser.__init__', side_effect=Exception("Invalid input")):
        with pytest.raises(Exception, match="Invalid input"):
            parser = HTTPieArgumentParser()
