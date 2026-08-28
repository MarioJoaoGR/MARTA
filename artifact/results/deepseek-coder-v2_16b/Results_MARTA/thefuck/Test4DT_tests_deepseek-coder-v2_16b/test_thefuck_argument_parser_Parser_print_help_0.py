
import pytest
from argparse import ArgumentParser
import sys
from thefuck.argument_parser import Parser



def test_invalid_input_error_handling():
    parser = Parser()
    with pytest.raises(SystemExit):
        parser._parser.parse_args(['--invalid-arg'])