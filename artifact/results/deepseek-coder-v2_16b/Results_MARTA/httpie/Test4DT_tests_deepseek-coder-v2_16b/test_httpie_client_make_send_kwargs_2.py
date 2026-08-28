
import pytest
import argparse
from httpie.client import make_send_kwargs

def test_no_timeout():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float)
    args = parser.parse_args([])
    result = make_send_kwargs(args)
    assert result == {'timeout': None, 'allow_redirects': False}

def test_with_timeout():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float)
    args = parser.parse_args(['--timeout', '5.0'])
    result = make_send_kwargs(args)
    assert result == {'timeout': 5.0, 'allow_redirects': False}

def test_custom_namespace():
    custom_args = argparse.Namespace(timeout=10.0)
    result = make_send_kwargs(custom_args)
    assert result == {'timeout': 10.0, 'allow_redirects': False}
