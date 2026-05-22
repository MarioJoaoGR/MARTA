
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

def test_edge_cases():
    with patch('httpie.cli.argparser.HTTPieArgumentParser.__init__', return_value=None):
        parser = HTTPieArgumentParser()

        # Test None as input
        with pytest.raises(AttributeError):
            args = parser.parse_args(env=MagicMock(), args=None)
