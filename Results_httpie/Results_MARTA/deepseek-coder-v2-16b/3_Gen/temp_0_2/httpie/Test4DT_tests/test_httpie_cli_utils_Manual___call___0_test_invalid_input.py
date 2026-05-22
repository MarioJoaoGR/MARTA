
import argparse
from httpie.cli.utils import Manual

def test_invalid_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manual', action=Manual, help='Prints the manual page.')
    
    # Test with invalid input to trigger the __call__ method
    try:
        parser.parse_args(['--invalid'])
    except SystemExit as e:
        assert e.code == 2  # argparse uses code 2 for argument errors
