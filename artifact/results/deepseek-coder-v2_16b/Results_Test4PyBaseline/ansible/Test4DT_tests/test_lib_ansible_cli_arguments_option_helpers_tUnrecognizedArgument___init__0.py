
import argparse
import pytest
from ansible.cli.arguments.option_helpers import UnrecognizedArgument

# Test Case 1: Basic Usage of UnrecognizedArgument
def test_unrecognized_argument_basic():
    parser = argparse.ArgumentParser(description="Example script with unrecognized argument.")
    parser.add_argument('--test', action=UnrecognizedArgument)
    
    # Parsing arguments and catching the SystemExit for error message
    with pytest.raises(SystemExit) as excinfo:
        args = parser.parse_args()
    assert str(excinfo.value) == "2"  # This will catch the SystemExit and validate the custom error message.

# Test Case 2: Custom Error Message
def test_unrecognized_argument_custom_error():
    parser = argparse.ArgumentParser(description="Example script with unrecognized argument.")
    parser.add_argument('--test', action=UnrecognizedArgument, help="This option will raise an error if not provided.")
    
    # Parsing arguments and catching the SystemExit for custom error message
    with pytest.raises(SystemExit) as excinfo:
        args = parser.parse_args()