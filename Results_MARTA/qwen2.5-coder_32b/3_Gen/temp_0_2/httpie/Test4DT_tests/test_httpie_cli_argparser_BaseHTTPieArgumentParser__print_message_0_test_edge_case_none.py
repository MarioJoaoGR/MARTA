
import sys
from unittest.mock import patch, MagicMock
import pytest
from httpie.cli.argparser import BaseHTTPieArgumentParser

@pytest.fixture
def parser():
    return BaseHTTPieArgumentParser()

def test_edge_case_none(parser):
    with patch('sys.stdout', new=MagicMock()) as mock_stdout:
        parser._print_message(None, file=sys.stdout)
        assert mock_stdout.write.called is False
