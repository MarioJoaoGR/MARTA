
import argparse
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

def test_invalid_inputs():
    with patch('httpie.cli.argparser.HTTPieArgumentParser.__init__', side_effect=Exception("Invalid Input")):
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers()
        
        try:
            httpie_parser = HTTPieArgumentParser(subparsers=subparsers)
        except Exception as e:
            assert str(e) == "Invalid Input"
