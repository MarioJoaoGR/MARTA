
import argparse
from unittest.mock import patch, MagicMock
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

@pytest.fixture(autouse=True)
def mock_httpie_argument_parser():
    with patch('httpie.cli.argparser.HTTPieArgumentParser', autospec=True):
        yield

def test_valid_inputs():
    parser = HTTPieArgumentParser()
    assert isinstance(parser, argparse.ArgumentParser)
