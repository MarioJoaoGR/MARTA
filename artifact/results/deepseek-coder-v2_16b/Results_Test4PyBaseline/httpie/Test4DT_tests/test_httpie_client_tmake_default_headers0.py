
# Module: httpie.client
import argparse
from requests_toolbelt.multipart.encoder import MultipartEncoder
import pytest
from httpie.client import make_default_headers, DEFAULT_UA, JSON_ACCEPT, JSON_CONTENT_TYPE, FORM_CONTENT_TYPE

def test_make_default_headers_json_no_files():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, help='Data payload for the request')
    parser.add_argument('--form', action='store_true', help='Send data as form')
    parser.add_argument('--json', action='store_true', help='Send data as JSON')
    parser.add_argument('--files', nargs='*', help='Files to be included in the request')
    
    args = parser.parse_args(['--data', 'some data', '--json'])
    headers = make_default_headers(args)
    
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE

def test_make_default_headers_form_no_files():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, help='Data payload for the request')
    parser.add_argument('--form', action='store_true', help='Send data as form')
    parser.add_argument('--json', action='store_true', help='Send data as JSON')
    parser.add_argument('--files', nargs='*', help='Files to be included in the request')
    
    args = parser.parse_args(['--data', 'some data', '--form'])
    headers = make_default_headers(args)
    
    assert headers['Content-Type'] == FORM_CONTENT_TYPE

def test_make_default_headers_json_with_files():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, help='Data payload for the request')
    parser.add_argument('--form', action='store_true', help='Send data as form')
    parser.add_argument('--json', action='store_true', help='Send data as JSON')
    parser.add_argument('--files', nargs='*', help='Files to be included in the request')
    
    args = parser.parse_args(['--data', 'some data', '--json', '--files', 'file1', 'file2'])
    headers = make_default_headers(args)
    
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE

if __name__ == "__main__":
    pytest.main()
