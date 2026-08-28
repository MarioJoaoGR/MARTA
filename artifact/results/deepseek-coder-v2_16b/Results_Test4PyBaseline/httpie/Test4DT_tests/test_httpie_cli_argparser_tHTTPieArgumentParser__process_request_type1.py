
import pytest
from httpie.cli.argparser import HTTPieArgumentParser, RequestType
import argparse  # Importing the module here since it's used in the code and not recognized by pylint

# Fixture to create an instance of HTTPieArgumentParser for testing
@pytest.fixture
def parser():
    return HTTPieArgumentParser()

# Test case to check if the request_type is correctly processed and sets the appropriate flags in args
def test_process_request_type(parser):
    # Set different values for request_type and check the corresponding flags in args
    
    parser.args = argparse.Namespace()  # Create a mock namespace for args
    parser.args.request_type = RequestType.JSON
    parser._process_request_type()
    assert parser.args.json is True
    assert parser.args.multipart is False
    assert parser.args.form is False

    parser.args.request_type = RequestType.MULTIPART
    parser._process_request_type()
    assert parser.args.json is False
    assert parser.args.multipart is True