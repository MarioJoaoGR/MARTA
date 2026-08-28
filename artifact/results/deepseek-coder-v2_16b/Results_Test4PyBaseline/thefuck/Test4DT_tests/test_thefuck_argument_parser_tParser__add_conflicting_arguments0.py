
import pytest
from thefuck.argument_parser import Parser
from argparse import Namespace

@pytest.fixture
def parser():
    return Parser()

def test_parse_args_with_version(parser):
    args = parser.parse(['--version'])
    assert isinstance(args, Namespace)