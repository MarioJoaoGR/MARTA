
import pytest
from unittest.mock import patch
from httpie.cli.argparser import HTTPieArgumentParser

def test_edge_case():
    with patch('httpie.cli.argparser.HTTPieArgumentParser.__init__', lambda self, *args, **kwargs: None):
        parser = HTTPieArgumentParser()
        assert not hasattr(parser, 'format_options')
