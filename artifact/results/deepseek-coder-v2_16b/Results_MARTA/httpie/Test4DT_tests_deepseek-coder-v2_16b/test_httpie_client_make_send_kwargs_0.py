
import argparse
import pytest
from unittest.mock import patch

def make_send_kwargs(args: argparse.Namespace) -> dict:
    kwargs = {
        'timeout': args.timeout or None,
        'allow_redirects': False,
    }
    return kwargs

# Test 1: test_valid_input_with_timeout
def test_valid_input_with_timeout():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float)
    args = parser.parse_args(['--timeout', '5.0'])
    
    result = make_send_kwargs(args)
    assert result == {'timeout': 5.0, 'allow_redirects': False}

# Test 2: test_no_timeout_specified
def test_no_timeout_specified():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float)
    args = parser.parse_args([])
    
    result = make_send_kwargs(args)
    assert result == {'timeout': None, 'allow_redirects': False}

# Test 3: test_invalid_input_negative_timeout
def test_invalid_input_negative_timeout():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float)
    args = parser.parse_args(['--timeout', '-5.0'])
    
    result = make_send_kwargs(args)
    assert result == {'timeout': -5.0, 'allow_redirects': False}
