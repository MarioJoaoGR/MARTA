
import pytest
from unittest.mock import patch
from httpie.cli.argparser import HTTPieArgumentParser, OUTPUT_OPTIONS, OUTPUT_OPTIONS_DEFAULT_OFFLINE, OUTPUT_OPTIONS_DEFAULT_STDOUT_REDIRECTED, OUTPUT_OPTIONS_DEFAULT, OUT_RESP_BODY


def test_httpie_argument_parser_process_output_options():
    with patch('argparse.ArgumentParser.__init__', return_value=None):
        parser = HTTPieArgumentParser()
        parser.args = type('Namespace', (object,), {'verbose': False, 'offline': False, 'download': False})()
        parser.env = type('Namespace', (object,), {'stdout_isatty': True})()
        with pytest.raises(AttributeError):
            parser._process_output_options()

def test_httpie_argument_parser_process_output_options_verbose():
    with patch('argparse.ArgumentParser.__init__', return_value=None):
        parser = HTTPieArgumentParser()
        parser.args = type('Namespace', (object,), {'verbose': True, 'offline': False, 'download': False})()
        parser.env = type('Namespace', (object,), {'stdout_isatty': True})()
        with pytest.raises(AttributeError):
            parser._process_output_options()

def test_httpie_argument_parser_process_output_options_offline():
    with patch('argparse.ArgumentParser.__init__', return_value=None):
        parser = HTTPieArgumentParser()
        parser.args = type('Namespace', (object,), {'verbose': False, 'offline': True, 'download': False})()
        parser.env = type('Namespace', (object,), {'stdout_isatty': True})()
        with pytest.raises(AttributeError):
            parser._process_output_options()

def test_httpie_argument_parser_process_output_options_stdout_redirected():
    with patch('argparse.ArgumentParser.__init__', return_value=None):
        parser = HTTPieArgumentParser()
        parser.args = type('Namespace', (object,), {'verbose': False, 'offline': False, 'download': False})()
        parser.env = type('Namespace', (object,), {'stdout_isatty': False})()
        with pytest.raises(AttributeError):
            parser._process_output_options()