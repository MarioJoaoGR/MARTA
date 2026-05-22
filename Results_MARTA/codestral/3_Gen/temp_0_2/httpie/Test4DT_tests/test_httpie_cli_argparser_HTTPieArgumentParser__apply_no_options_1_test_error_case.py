
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

def test_error_case():
    with patch('httpie.cli.argparser.HTTPieArgumentParser.__init__', side_effect=Exception("Invalid argument")):
        with pytest.raises(Exception, match="Invalid argument"):
            parser = HTTPieArgumentParser()
