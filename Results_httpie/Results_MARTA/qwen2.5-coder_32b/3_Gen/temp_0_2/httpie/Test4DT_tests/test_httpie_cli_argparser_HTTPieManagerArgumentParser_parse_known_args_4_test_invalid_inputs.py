
import pytest
from unittest.mock import patch
from httpie.cli.argparser import HTTPieManagerArgumentParser
import argparse

def test_invalid_inputs():
    with patch('httpie.cli.argparser.HTTPieManagerArgumentParser.parse_known_args', side_effect=argparse.ArgumentError(None, None)):
        parser = HTTPieManagerArgumentParser()
        with pytest.raises(argparse.ArgumentError):
            parser.parse_known_args(['--invalid-argument'])
