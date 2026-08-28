
import pytest
from argparse import ArgumentParser
from unittest.mock import patch
from thefuck.argument_parser import Parser

@pytest.fixture(autouse=True)
def parser():
    return Parser()


def test_alias_argument(parser):
    with patch('argparse.ArgumentParser.parse_args') as mock_parse_args:
        mock_parse_args.return_value = ArgumentParser().parse_args(['script_name', '-a'])
        assert parser._parser.parse_args()['alias'] is not None



