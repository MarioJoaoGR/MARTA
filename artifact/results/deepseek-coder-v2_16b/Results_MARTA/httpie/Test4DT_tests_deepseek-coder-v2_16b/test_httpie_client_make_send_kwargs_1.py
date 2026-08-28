
import argparse
import pytest

def make_send_kwargs(args: argparse.Namespace) -> dict:
    kwargs = {
        'timeout': args.timeout or None,
        'allow_redirects': False,
    }
    return kwargs

# Test 1: test_valid_inputs
def test_valid_inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float)
    args = parser.parse_args(['--timeout', '5.0'])
    
    result = make_send_kwargs(args)
    assert result == {'timeout': 5.0, 'allow_redirects': False}

# Test 2: test_missing_timeout
def test_missing_timeout():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float)
    args = parser.parse_args([])
    
    result = make_send_kwargs(args)
    assert result == {'timeout': None, 'allow_redirects': False}

# Test 3: test_invalid_inputs
def test_invalid_inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=float)
    with pytest.raises(SystemExit):
        args = parser.parse_args(['--timeout', 'not a float'])
