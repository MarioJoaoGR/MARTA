
import argparse
import pytest
from unittest.mock import patch
from httpie.client import make_send_kwargs

def test_make_send_kwargs_no_timeout():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float, help='Timeout for the request')
    args = parser.parse_args([])
    
    with patch('httpie.client.make_send_kwargs', return_value={'timeout': None, 'allow_redirects': False}):
        send_kwargs = make_send_kwargs(args)
        assert send_kwargs == {'timeout': None, 'allow_redirects': False}

def test_make_send_kwargs_with_timeout():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float, help='Timeout for the request')
    args = parser.parse_args(['--timeout', '5.0'])
    
    with patch('httpie.client.make_send_kwargs', return_value={'timeout': 5.0, 'allow_redirects': False}):
        send_kwargs = make_send_kwargs(args)
        assert send_kwargs == {'timeout': 5.0, 'allow_redirects': False}

def test_make_send_kwargs_custom_namespace():
    custom_args = argparse.Namespace(timeout=10.0)
    
    with patch('httpie.client.make_send_kwargs', return_value={'timeout': 10.0, 'allow_redirects': False}):
        send_kwargs = make_send_kwargs(custom_args)
        assert send_kwargs == {'timeout': 10.0, 'allow_redirects': False}
