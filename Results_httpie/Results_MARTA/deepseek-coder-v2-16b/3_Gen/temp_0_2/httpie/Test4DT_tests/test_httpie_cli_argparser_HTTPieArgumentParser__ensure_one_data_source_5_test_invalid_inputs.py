
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

def test_invalid_inputs():
    with patch('httpie.cli.argparser.HTTPieArgumentParser._ensure_one_data_source', side_effect=ValueError("Invalid input")):
        parser = HTTPieArgumentParser()
        with pytest.raises(ValueError):
            parser._ensure_one_data_source()
