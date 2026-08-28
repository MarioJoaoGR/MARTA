
import pytest
from httpie.cli.argparser import HTTPieArgumentParser
from argparse import ArgumentParser

# Fixture to create an instance of HTTPieArgumentParser for testing
@pytest.fixture
def parser():
    return HTTPieArgumentParser()

# Test case to check if the parser is initialized correctly without any arguments
def test_parser_initialization(parser):
    assert isinstance(parser, ArgumentParser)