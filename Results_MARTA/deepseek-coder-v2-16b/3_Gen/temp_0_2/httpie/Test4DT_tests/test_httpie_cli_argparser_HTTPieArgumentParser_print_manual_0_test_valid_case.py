
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

@pytest.fixture
def parser():
    return HTTPieArgumentParser()

def test_print_manual(parser):
    with patch('httpie.output.ui.man_pages.display_for') as mock_display:
        mock_display.return_value = None
        parser.env = MagicMock()
        parser.env.program_name = 'http'
        parser.print_manual()
        assert mock_display.called_once_with(parser.env, 'http')
