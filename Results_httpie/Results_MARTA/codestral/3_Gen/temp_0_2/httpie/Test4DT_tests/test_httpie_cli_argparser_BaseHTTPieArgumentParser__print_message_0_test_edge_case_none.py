
import sys
from unittest.mock import patch, MagicMock
import pytest
from httpie.cli.argparser import BaseHTTPieArgumentParser

@pytest.fixture(autouse=True)
def setup_parser():
    parser = BaseHTTPieArgumentParser()
    return parser

def test_edge_case_none(setup_parser):
    with patch('sys.stdout', new_callable=MagicMock) as mock_stdout:
        setup_parser._print_message(None, file=sys.stdout)
        assert not mock_stdout.called
