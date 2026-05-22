
import argparse
from httpie.client import HTTPHeadersDict
from unittest.mock import patch

# Assuming DEFAULT_UA, JSON_ACCEPT, JSON_CONTENT_TYPE, and FORM_CONTENT_TYPE are defined somewhere in your codebase
DEFAULT_UA = "TestUA/1.0"
JSON_ACCEPT = "application/json"
JSON_CONTENT_TYPE = "application/json"
FORM_CONTENT_TYPE = "application/x-www-form-urlencoded"

def make_default_headers(args: argparse.Namespace) -> HTTPHeadersDict:
    default_headers = HTTPHeadersDict({
        'User-Agent': DEFAULT_UA
    })

    auto_json = args.data and not args.form
    if args.json or auto_json:
        default_headers['Accept'] = JSON_ACCEPT
        if args.json or (auto_json and args.data):
            default_headers['Content-Type'] = JSON_CONTENT_TYPE

    elif args.form and not args.files:
        # If sending files, `requests` will set
        # the `Content-Type` for us.
        default_headers['Content-Type'] = FORM_CONTENT_TYPE
    return default_headers

# Example test case using unittest.mock.patch to mock argparse and HTTPHeadersDict
def test_make_default_headers():
    with patch('argparse.Namespace', autospec=True) as mock_args:
        mock_args.json = True
        mock_args.data = False
        mock_args.form = False
        mock_args.files = False

        headers = make_default_headers(mock_args)
        assert 'Accept' in headers
        assert headers['Accept'] == JSON_ACCEPT
        assert 'Content-Type' in headers
        assert headers['Content-Type'] == JSON_CONTENT_TYPE

# Run the test if this script is executed directly
if __name__ == "__main__":
    test_make_default_headers()
