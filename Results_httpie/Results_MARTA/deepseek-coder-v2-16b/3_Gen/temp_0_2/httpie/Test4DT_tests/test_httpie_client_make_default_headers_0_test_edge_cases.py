
import argparse
from httpie.client import HTTPHeadersDict
from unittest.mock import patch, MagicMock

# Assuming DEFAULT_UA, JSON_ACCEPT, JSON_CONTENT_TYPE, and FORM_CONTENT_TYPE are defined elsewhere in your module or imported from a config file
DEFAULT_UA = "your_default_user_agent"
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

# Test case to check edge cases
def test_edge_cases():
    with patch('httpie.client.HTTPHeadersDict', MagicMock):
        args = argparse.Namespace(json=True, data=False, form=False, files=False)
        
        headers = make_default_headers(args)
        
        assert 'User-Agent' in headers
        assert headers['User-Agent'] == DEFAULT_UA
        
        if args.json or (not args.form and not args.files):
            assert 'Accept' in headers
            assert headers['Accept'] == JSON_ACCEPT
            
            assert 'Content-Type' in headers
            assert headers['Content-Type'] == JSON_CONTENT_TYPE
        
        if args.form and not args.files:
            assert 'Content-Type' in headers
            assert headers['Content-Type'] == FORM_CONTENT_TYPE
