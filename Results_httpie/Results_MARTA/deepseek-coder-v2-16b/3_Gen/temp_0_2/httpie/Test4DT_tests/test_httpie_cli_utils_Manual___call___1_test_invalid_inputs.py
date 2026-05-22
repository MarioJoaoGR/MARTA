
import argparse
from httpie.cli.utils import Manual

def test_invalid_inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manual', action=Manual, help='Prints the manual page.')
    
    # Test with invalid inputs to ensure they raise errors as expected
    try:
        parser.parse_args(['--invalid'])
    except SystemExit as e:
        assert e.code != 0  # Ensure that parsing an invalid argument raises a non-zero exit code
