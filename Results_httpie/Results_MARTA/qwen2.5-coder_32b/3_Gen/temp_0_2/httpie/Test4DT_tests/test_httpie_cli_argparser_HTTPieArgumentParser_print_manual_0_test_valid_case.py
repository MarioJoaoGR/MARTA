
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

def test_print_manual():
    with patch('httpie.output.ui.man_pages.is_available') as is_available_mock, \
         patch('httpie.output.ui.man_pages.display_for') as display_for_mock:

        parser = HTTPieArgumentParser()
        parser.env = MagicMock()
        parser.env.program_name = 'http'

        is_available_mock.return_value = True

        parser.print_manual()

        assert is_available_mock.called
        assert display_for_mock.called

    with patch('httpie.output.ui.man_pages.is_available') as is_available_mock, \
         patch('httpie.output.ui.man_pages.display_for') as display_for_mock:

        parser = HTTPieArgumentParser()
        parser.env = MagicMock()
        parser.env.program_name = 'http'

        is_available_mock.return_value = False
        text = "Help message"
        with patch('argparse.ArgumentParser.format_help', return_value=text):
            parser.print_manual()
