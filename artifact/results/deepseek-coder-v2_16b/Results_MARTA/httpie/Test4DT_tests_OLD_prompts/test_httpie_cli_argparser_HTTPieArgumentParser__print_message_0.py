
import pytest
from httpie.cli.argparser import HTTPieArgumentParser
from unittest.mock import patch
import sys
import os

def test_default_initialization():
    with patch('sys.stdout', new=open(os.devnull, 'w')):
        parser = HTTPieArgumentParser()
        assert hasattr(parser, 'env')
        assert hasattr(parser, 'args')
        assert hasattr(parser, 'has_stdin_data')
