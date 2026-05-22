
import argparse
from httpie.cli.argparser import HTTPieArgumentParser
from unittest.mock import patch

def test_edge_case():
    with patch('httpie.cli.argparser.HTTPieArgumentParser.__init__', lambda self, *args, **kwargs: None):
        parser = HTTPieArgumentParser()
        assert hasattr(parser, 'args') is False
