
import pytest
from unittest.mock import patch
from httpie.cli.argparser import HTTPieArgumentParser

@patch('httpie.cli.argparser.HTTPieArgumentParser._process_url', autospec=True)
def test_curl_style_shorthand(mock_process_url):
    parser = HTTPieArgumentParser()
    with pytest.raises(AttributeError):  # This is a mock of the expected error
        args = parser.parse_args(['--url', ':3000/foo'])
