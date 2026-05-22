
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

def test_invalid_inputs():
    with patch('httpie.cli.argparser.HTTPieArgumentParser.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            parser = HTTPieArgumentParser()
