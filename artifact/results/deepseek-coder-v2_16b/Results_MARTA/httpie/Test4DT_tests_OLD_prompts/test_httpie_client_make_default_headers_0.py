
import pytest
from httpie.client import make_default_headers
import argparse
from unittest.mock import patch

def test_make_default_headers_json():
    args = argparse.Namespace(data=True, form=False, json=True, files=False)
    with patch('httpie.client.DEFAULT_UA', 'DEFAULT_UA'):
        with patch('httpie.client.JSON_ACCEPT', 'JSON_ACCEPT'):
            with patch('httpie.client.JSON_CONTENT_TYPE', 'JSON_CONTENT_TYPE'):
                headers = make_default_headers(args)
                assert headers == {'User-Agent': 'DEFAULT_UA', 'Accept': 'JSON_ACCEPT', 'Content-Type': 'JSON_CONTENT_TYPE'}

def test_make_default_headers_form():
    args = argparse.Namespace(data=True, form=True, json=False, files=False)
    with patch('httpie.client.DEFAULT_UA', 'DEFAULT_UA'):
        with patch('httpie.client.FORM_CONTENT_TYPE', 'FORM_CONTENT_TYPE'):
            headers = make_default_headers(args)
            assert headers == {'User-Agent': 'DEFAULT_UA', 'Content-Type': 'FORM_CONTENT_TYPE'}

def test_make_default_headers_auto_json():
    args = argparse.Namespace(data=True, form=False, json=True, files=False)
    with patch('httpie.client.DEFAULT_UA', 'DEFAULT_UA'):
        with patch('httpie.client.JSON_ACCEPT', 'JSON_ACCEPT'):
            with patch('httpie.client.JSON_CONTENT_TYPE', 'JSON_CONTENT_TYPE'):
                headers = make_default_headers(args)
                assert headers == {'User-Agent': 'DEFAULT_UA', 'Accept': 'JSON_ACCEPT', 'Content-Type': 'JSON_CONTENT_TYPE'}

def test_make_default_headers_form_no_files():
    args = argparse.Namespace(data=True, form=True, json=False, files=False)
    with patch('httpie.client.DEFAULT_UA', 'DEFAULT_UA'):
        with patch('httpie.client.FORM_CONTENT_TYPE', 'FORM_CONTENT_TYPE'):
            headers = make_default_headers(args)
            assert headers == {'User-Agent': 'DEFAULT_UA', 'Content-Type': 'FORM_CONTENT_TYPE'}
