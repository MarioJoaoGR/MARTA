
import pytest
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.context import Environment
import argparse

def test_HTTPieArgumentParser_initialization():
    parser = HTTPieArgumentParser()
    assert isinstance(parser, argparse.ArgumentParser), "Expected parser to be an instance of argparse.ArgumentParser"
    assert not parser.add_help, "Expected add_help to be False after initialization"



